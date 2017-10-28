import csv
import json

csvfile = open('pharmacyList.csv', 'r')
jsonfile = open('pharmacyList.json', 'w')
j =[]
fieldnames = ('name','line-1','line-2','city','pin','state','country','phoneNumber','email','first name','last name','drugLicenceNumber','GSTNo','registrationDate','numberOfUsers','active','expiry','lastlogin')
reader = csv.DictReader( csvfile, fieldnames)

for row in reader:
    row["_id"]=row['name']
    row["address"] =  {
        "line1" : row["line-1"],
        "line2" : row["line-2"],
        "city": row["city"],
        "pin": row["pin"],
        "state": row["state"],
        "country": row["country"]
    }
    row["owner"] = {
        "firstName": row["first name"],
        "lastName": row["last name"]
    }
    del (row["line-1"])
    del (row["line-2"])
    del (row["city"])
    del (row["pin"])
    del (row["state"])
    del (row["country"])
    del (row["first name"])
    del (row["last name"])
    j.append(row)
json.dump(j, jsonfile)
