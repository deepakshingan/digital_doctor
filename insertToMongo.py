import json
import pymongo
from pprint import pprint

connection = pymongo.MongoClient("mongodb://localhost")
db=connection.drIndian
record1 = db.drIndian

with open('file.json') as data_file:
    data = json.load(data_file)
    for record in data:
        record1.insert_one(record)

