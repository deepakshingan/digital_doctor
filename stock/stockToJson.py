import csv
import json

csvfile = open('stock_data_2016.csv', 'r')
jsonfile = open('stock_data_2016.json', 'w')
j =[]
fieldnames = ('Date','Particulars','Voucher No.','Bill No','Amount')
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    row["transaction"] = [ {
        "date" : row["Date"],
        "voucherNo" : row["Voucher No."],
        "billNo": row["Bill No"],
        "Amount":{
            "total" : row['Amount'],
            "status" : "paid",
            "installments" : [{"date": "20-10-2017", "paid" : float(100)},
                              {"date": "21-10-2017", "paid": float(100)},
                              {"date": "22-10-2017", "paid": float(100)}]
        }
    }]
    row['Name'] = row['Particulars']
    del (row["Particulars"])
    del (row["Date"])
    del (row["Voucher No."])
    del (row["Bill No"])
    del (row["Amount"])
    j.append(row)
json.dump(j, jsonfile)
