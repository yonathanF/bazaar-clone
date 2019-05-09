from pyspark import SparkContext

from operator import add

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log", 2)     # each worker loads a piece of the data file

# Step 1
pairs = data.map(lambda line: line.split(" "))   # tell each worker to split each line of it's partition

# Step 2
group_users = pairs.groupByKey().mapValues(list)

# Step 3
#item_pairs = group_users.flatMap(lambda x: )
item_pairs = group_users.map(lambda x: (x[0], list(zip([0] +x[1], x[1]))))

item_pairs_deleted = item_pairs.map(lambda x: (x[0], x[1][1:]))

# Step 4
def f(x): return x


def g(x):
    result = []
    for i in x:
        result.append((i[0], 1))
    return result 

pair_to_user = item_pairs_deleted.flatMapValues(f).groupBy(lambda x: x[1])
extract_user = pair_to_user.map(lambda x: (x[0], g(x[1])))

# Step 5

group2 = extract_user.groupBy(lambda x: x[1])
#distinct_users = group2.distinct()
#distinct_users = extract_user.map(lambda x: (x[0], len(set(x[1]))))

# Step 6

#filtered_users = distinct_users.filter(lambda x: x[1] >= 3)


#pages = pairs.map(lambda pair: (pair[0], 1))      # re-layout the data to ignore the user id
#count = pages.reduceByKey(lambda x,y: int(x)+int(y))  # and then reduce all the values by adding them together

output = extract_user.collect()                          # bring the data back to the master node so we can print it out
#output2 = group2.collect()

print(output)
#print(output2)
#for page_id in output:
#    print(page_id)
#    print ("page_id %s count %d" % (page_id, count))
#print ("Popular items done")

sc.stop()
