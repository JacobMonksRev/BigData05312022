#kafka_producer_avro.py
from confluent_kafka import Producer
from avro import schema
import avro.io
import io

from datetime import datetime
import time
import random

# pip install avro-python3
# pip install confluent-kafka

KAFKA_TOPIC_NAME_CONS = "test-topic"
KAFKA_BOOTSTRAP_SERVERS_CONS = 'localhost:9092'

if __name__ == "__main__":
    print("Kafka Producer Application Started ... ")

    kafka_config_obj = {'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS_CONS}
    kafka_producer_obj = Producer(**kafka_config_obj)

    product_name_list = ["Laptop", "Desktop Computer", "Mobile Phone", "Wrist Band", "Wrist Watch", "LAN Cable",
                         "HDMI Cable", "TV", "TV Stand", "Text Books", "External Hard Drive", "Pen Drive", "Online Course"]

    order_card_type_list = ["Visa", "MasterCard", "Maestro"]

    country_name_city_name_list = ["Sydney,Australia", "Florida,United States", "New York City,United States",
                                   "Paris,France", "Colombo,Sri Lanka", "Dhaka,Bangladesh", "Islamabad,Pakistan",
                                   "Beijing,China", "Rome,Italy", "Berlin,Germany", "Ottawa,Canada",
                                   "London,United Kingdom", "Jerusalem,Israel", "Bangkok,Thailand",
                                   "Chennai,India", "Bangalore,India", "Mumbai,India", "Pune,India",
                                   "New Delhi,Inida", "Hyderabad,India", "Kolkata,India", "Singapore,Singapore"]

    ecommerce_website_name_list = ["www.datamaking.com", "www.amazon.com", "www.flipkart.com", "www.snapdeal.com", "www.ebay.com"]

    # Path to user.avsc avro schema
    avro_schema_path = "/home/hdoop/SparkSamples/OrderData/orders.avsc"
    avro_orders_schema = schema.Parse(open(avro_schema_path).read())

    message_list = []
    message = None
    for i in range(500):
        i = i + 1
        message = {}
        print("Preparing message: " + str(i))
        event_datetime = datetime.now()

        message["order_id"] = i
        message["order_product_name"] = random.choice(product_name_list)
        message["order_card_type"] = random.choice(order_card_type_list)
        message["order_amount"] = round(random.uniform(5.5, 555.5), 2)
        message["order_datetime"] = event_datetime.strftime("%Y-%m-%d %H:%M:%S")
        country_name = None
        city_name = None
        country_name_city_name = None
        country_name_city_name = random.choice(country_name_city_name_list)
        country_name = country_name_city_name.split(",")[1]
        city_name = country_name_city_name.split(",")[0]
        message["order_country_name"] = country_name
        message["order_city_name"] = city_name
        message["order_ecommerce_website_name"] = random.choice(ecommerce_website_name_list)

        # order_id,order_product_name,order_card_type,order_amount,order_datetime,order_country_name,order_city_name,order_ecommerce_website_name
        # print("Message Type: ", type(message))
        print("Message: ", message)
        #message_list.append(message)
        message_writer = avro.io.DatumWriter(avro_orders_schema)
        message_bytes_writer = io.BytesIO()
        message_encoder = avro.io.BinaryEncoder(message_bytes_writer)
        message_writer.write(message, message_encoder)
        message_raw_bytes = message_bytes_writer.getvalue()
        kafka_producer_obj.produce(KAFKA_TOPIC_NAME_CONS, message_raw_bytes)
        time.sleep(1)

    kafka_producer_obj.flush()
    # print(message_list)

    print("Kafka Producer Application Completed. ")
    
