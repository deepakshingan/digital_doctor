import json
import pymongo
from pprint import pprint

connection = pymongo.MongoClient("mongodb://localhost")
db=connection.drIndian
targetConnection = pymongo.MongoClient("mongodb://drmongoadmin:androidapp@35.197.135.179")
targetDb=targetConnection.medicines_db

tempCollection = db.temp_2016
parsedDuplicateData = []
for record in tempCollection.find({}):
    record['_id'] = record["Name"]
    record["medicineType"] = 'brand'
    record['referencedGenericMedicine'] = []
    record['manufacturer']=''
    record['ATC Classification'] = []
    record['contents'] = ''
    record['CIMSClass'] = ''
    if(tempCollection.find({"Name":record["Name"]}).count()==1):
        targetDb.companyMedicine.insert(record)
    else:
        if not( record["Name"] in parsedDuplicateData):
            recordsWithSameName = tempCollection.find({"Name": record["Name"]})
            presentationArray = []
            for duplicateRecord in recordsWithSameName:
                presentationArray = presentationArray + duplicateRecord['presentation']
            correctRecord = {}
            correctRecord['Name'] = record["Name"]
            correctRecord['presentation'] = presentationArray
            targetDb.companyMedicine.insert(correctRecord)
            parsedDuplicateData.append(record["Name"])