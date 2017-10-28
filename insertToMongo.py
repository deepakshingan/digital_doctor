import json
import pymongo
from pprint import pprint

#connection = pymongo.MongoClient("mongodb://localhost")
connection = pymongo.MongoClient("mongodb://drmongoadmin:androidapp@35.197.135.179")
db=connection.medical_users
record1 = db.pharmacy

with open('pharmacyList.json') as data_file:
    data = json.load(data_file)
    for record in data:
        record1.insert_one(record)

