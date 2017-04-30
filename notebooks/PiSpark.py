
# coding: utf-8

# In[2]:

import pyspark
from pyspark.context import SparkContext
from pyspark.sql import SparkSession, SQLContext


# In[ ]:

spark = SparkSession.builder.appName("PythonPi").getOrCreate()

#TODO: Need to get this value from querystring 'partitions'
partitions = 2
n = 100000 * partitions

def f(_):
    x = random() * 2 - 1
    y = random() * 2 - 1
    return 1 if x ** 2 + y ** 2 <= 1 else 0

count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
print("Pi is roughly %f" % (4.0 * count / n))

spark.stop()
 

