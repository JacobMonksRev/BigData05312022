# pyspark_job.py
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
def create_spark_session():
    """Create spark session.
Returns:
        spark (SparkSession) - spark session connected to AWS EMR
            cluster
    """
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages",
                "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark
def process_book_data(spark, input_path, output_path):
    """Process the book review data and write to S3.
Arguments:
        spark (SparkSession) - spark session connected to AWS EMR
            cluster
        input_path (str) - AWS S3 bucket path for source data
        output_path (str) - AWS S3 bucket for writing processed data
    """
    df = spark.read.parquet(input_path)
    # Apply some basic filters and aggregate by product_title.
    book_agg = df.filter(df.verified_purchase == 'Y') \
        .groupBy('product_title') \
        .agg({'star_rating': 'avg', 'review_id': 'count'}) \
        .filter(F.col('count(review_id)') >= 500) \
        .sort(F.desc('avg(star_rating)')) \
        .select(F.col('product_title').alias('book_title'),
                F.col('count(review_id)').alias('review_count'),
                F.col('avg(star_rating)').alias('review_avg_stars'))
    # Save the data to your S3 bucket as a .parquet file.
    book_agg.write.mode('overwrite')\
        .save(output_path)
def main():
    spark = create_spark_session()
    input_path = ('s3://amazon-reviews-pds/parquet/' +
                  'product_category=Books/*.parquet')
    output_path = 's3://spark-tutorial-bwl/book-aggregates'
    process_book_data(spark, input_path, output_path)
if __name__ == '__main__':
    main()