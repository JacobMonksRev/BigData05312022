import os
import sys
import time
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
# The following Kafkautils package requires pyspark version 2.4.6 or earlier.
# You can change your pyspark version using 'pip install --force-reinstall pyspark==2.4.6
# HOWEVER, this creates another issue where the import for SparkSession creates a TypeError that is built into the module.
# I am still working on finding a fix for this.
from pyspark.streaming.kafka import KafkaUtils

n_secs = 1
topic = "pyspark-kafka-demo"

conf = SparkConf().setAppName("KafkaStreamProcessor").setMaster("local[*]")
sc = SparkContext(conf)
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, n_secs)

kafkaStream = KafkaUtils.createDirectStream(ssc, [topic], {
    'bootstrap.servers':'localhost:9092',
    'group.id':'video-group',
    'fetch.message.max.bytes':'15728640',
    'auto.offset.reset':'largest'
})

ssc.start()
time.sleep(600) # runs for 600 seconds (10 minutes)
ssc.stop(stopSparkContext=True, stopGraceFully=True)