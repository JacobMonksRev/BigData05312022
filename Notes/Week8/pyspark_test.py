from pyspark import SparkContext as sc, sql, SparkConf
from pyspark.sql import SparkSession, Row
import pyspark

# Create a SparkSession variable
spark = SparkSession\
    .builder\
    .master("local[1]")\
    .appName("Put appname here")\
    .getOrCreate()

df1 = spark.createDataFrame()

rdd = sc.parallelize([1,2,3,4])