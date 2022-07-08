from pyspark import SparkContext, sql, SparkConf
from pyspark.sql import SparkSession, Row

# Create a SparkSession variable
spark = SparkSession\
    .builder\
    .appName("Put appname here")\
    .getOrCreate()