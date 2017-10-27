#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getopt, sys, io
import re

infile = open('input_sahayog_medicals/DATA_01_10_2016.txt')
while True:
    l = infile.readline()
    if l == "": break
    sub = l[60: 65]
    if(sub.strip() == ""):
        l = l[:60] + '0' + l[60:]
    result = re.sub('  +',',',l)
    with open('data_2016.csv', 'a') as the_file:
        the_file.write(result)

