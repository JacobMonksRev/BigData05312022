#run this code from CLI using spark-submit:
# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 file_name.py

from os import truncate
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.sql.functions import *
from pyspark.sql.types import *

if __name__ == '__main__':
    spark = SparkSession\
        .builder\
        .appName("Kafka-Pyspark-Example")\
        .master("local[*]")\
        .getOrCreate()

    KAFKA_TOPIC_NAME = "pyspark-kafka-demo"
    KAFKA_BOOTSTRAP_SERVER = "localhost:9092"
    sampleDataframe = (
        spark.readStream.format("kafka")
            .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVER)
            .option("subscribe", KAFKA_TOPIC_NAME)
            .option("startingOffsets", "latest")
            .load()

        )
    
    base_df = sampleDataframe.selectExpr("CAST(value as STRING)", "timestamp")
    base_df.printSchema()
    base_df.createOrReplaceTempView("test")

    result = base_df\
        .writeStream\
        .outputMode("append")\
        .format("console")\
        .start(truncate=False)

    result.awaitTermination()
    