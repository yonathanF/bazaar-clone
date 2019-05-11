import json

import requests

from pyspark import SparkContext

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access_log.log",
                   2)  # each worker loads a piece of the data file

# Step 1
pairs = data.map(lambda line: line.split(" "))

# Step 2
group_users = pairs.groupByKey().mapValues(list)

# Step 3
item_pairs = group_users.map(lambda x: (x[0], list(zip([0] + x[1], x[1]))))

item_pairs_deleted = item_pairs.map(lambda x: (x[0], x[1][1:]))


# Step 4
def f(x):
    return x


def g(x):
    result = []
    for i in x:
        result.append(i[0])
    return result


pair_to_user = item_pairs_deleted.flatMapValues(f).groupBy(lambda x: x[1])
extract_user = pair_to_user.map(lambda x: (x[0], g(x[1])))

# Step 5
distinct_users = extract_user.map(lambda x: (x[0], len(set(x[1]))))

# Step 6
filtered_users = distinct_users.filter(lambda x: x[1] >= 1)

output = filtered_users.collect()

recs = {}
for rec in output:
    if rec[0][0] in recs:
        recs[rec[0][0]].append(int(rec[0][1]))
    else:
        recs[rec[0][0]] = [int(rec[0][1])]

url = 'http://models-api:8000/api/v1/post/rec/'
post_fields = {'recs': json.dumps(recs)}

request = requests.post(url, data=post_fields)
sample_output = open("/tmp/data/sample_output.txt", "w")
sample_output.write(str(output))
sample_output.write("--------------------")
sample_output.write(str(post_fields))
sample_output.close()
sc.stop()
