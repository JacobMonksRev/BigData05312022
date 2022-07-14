from pyspark import SparkContext, sql, SparkConf
from pyspark.sql import SparkSession, Row, HiveContext, SQLContext
import pyspark
from pyspark.sql.functions import col
import os
import sys

## Set up PySpark Environment Variables
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

## Create a SparkSession variable
spark = SparkSession\
    .builder\
    .appName("App Name")\
    .master("local[*]")\
    .getOrCreate()

## .getOrCreate will either create a new SparkSession or search for the current one.
## SparkContext is a part of SparkSession, so we can initialize SparkContext and call it 'sc':
sc = spark.sparkContext

## If we wish to initialize SQLContext:
sqlcontext = SQLContext(spark)

## We can use 'sc' to create RDDs and DataFrames
rdd = sc.parallelize([(1,"Jacob","IT"),(2,"Bob","Sales"),(3,"Sam","IT"),(4,"Cindy","HR")])
df = rdd.toDF(["ID","Name","Dept"])
#df.show()
#df2 = spark.read.option('header','true').csv('Notes/Week8/sample.csv')
#df2.show()

## And we can query the DataFrame
#df.select("*").where(col("ID")=="1").show()

## Query using Spark SQL
# Spark SQL cannot query DataFrames directly, we must create a Temporary View
#df2.createOrReplaceTempView("NamesDF")
df.createOrReplaceTempView("Employees")
# Creates a temporary view that gets saved in Hive Metastore
spark.sql("SELECT Dept, count(*) FROM Employees GROUP BY Dept").show()