import csv
import json

csvfile = open('data_2016.csv', 'r')
jsonfile = open('file_2016.json', 'w')
j =[]
fieldnames = ('Name','Unit',	'Qty',	'Free',	'Amount')
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    row["presentation"] = [ {
        "type" : row["Unit"],
        "quantity" : row["Qty"],
        "price": row["Amount"],
        "batch":"0"
    }]
    del (row["Free"])
    del (row["Amount"])
    del (row["Unit"])
    del (row["Qty"])
    j.append(row)
json.dump(j, jsonfile)
