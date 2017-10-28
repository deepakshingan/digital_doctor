import json
import pymongo
from pprint import pprint

connection = pymongo.MongoClient("mongodb://localhost")
db=connection.drIndian
#targetConnection = pymongo.MongoClient("mongodb://localhost")
targetConnection = pymongo.MongoClient("mongodb://drmongoadmin:androidapp@35.197.135.179")
targetDb=targetConnection.medicines_db
tempCollection = db.temp_stock
parsedDuplicateData = []
for record in tempCollection.find({}):
    record['_id'] = record["Name"]
    record['address'] = { "line1" : "Shivajinagar", "line2":"","pin":"413411","city":"pune","state":"maharashtra","country":"india"}
    record["phone"] = ""
    record['email'] = ""
    record['GSTNo']=''
    if(tempCollection.find({"Name":record["Name"]}).count()==1):
        targetDb.stock.insert(record)
    else:
        if not( record["Name"] in parsedDuplicateData):
            recordsWithSameName = tempCollection.find({"Name": record["Name"]})
            transactionArray = []
            for duplicateRecord in recordsWithSameName:
                transactionArray = transactionArray + duplicateRecord['transaction']
            record['transaction'] = transactionArray
            targetDb.stock.insert(record)
            parsedDuplicateData.append(record["Name"])