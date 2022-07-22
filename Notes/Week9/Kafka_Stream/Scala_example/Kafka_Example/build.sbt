name := "Kafka Streaming Example"
version:= "1.0"
scalaVersion:= "2.11.12"

// Library Dependencies can be found at https://mvnrepository.com/
// Search for 'spark', 'hive', or 'kafka' in the search bar to find the relevant dependencies

libraryDependencies ++= Seq("org.apache.spark" %% "spark-sql" % "2.3.2",
                            "org.apache.spark" %% "spark-sql-kafka-0-10" % "2.3.2",
                            "org.apache.kafka" % "kafka-clients" % "2.6.0")