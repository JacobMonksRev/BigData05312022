import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.DataFrame
import org.apache.spark.SparkConf

object KafkaSparkExample {
    def main(args: Array[String]): Unit = {
        
        val spark = SparkSession
            .builder
            .appName("Kafka Example")
            .master("local[*]")
            .getOrCreate()

        spark.sparkContext.setLogLevel("WARN")
        import spark.implicits._

        val rdd = spark.sparkContext.parallelize(Seq(("Jacob",30),("Mary",43),("Bob",24)))
        val df = rdd.toDF("name","age")

        df.selectExpr("CAST(name AS String) AS key", "CAST(age AS String) AS value")
            .write
            .format("kafka")
            .option("topic","test-Topic")
            .option("kafka.bootstrap.servers","localhost:9092")
            .option("checkpointLocation", "/home/jacob/Checkpoint")
            .save()

        spark.close()
    }
}
