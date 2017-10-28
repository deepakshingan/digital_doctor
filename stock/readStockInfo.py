import re

infile = open('../input_sahayog_medicals/STOCK_INFO.txt')
while True:
    l = infile.readline()
    if l == "": break
    result = re.sub('  +',',',l)
    with open('stock_data_2016.csv', 'a') as the_file:
        the_file.write(result)

