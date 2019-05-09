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

print(output)

sc.stop()
