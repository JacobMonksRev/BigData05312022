from pymongo import MongoClient, mongo_client
from pprint import pprint

client = MongoClient('localhost', 27017)

db_mydb = client.mydb

name1 = db_mydb.Names.find_one({"first_name":"Jacob"})
print(name1)
name2 = db_mydb.Names.find()

for doc in name2:
    pprint(doc)