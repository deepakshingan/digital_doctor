#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getopt, sys, io
import re

def usage():
    print("usage: %s -n <spacenum> [-i] [infile]", sys.argv[0])
    exit(1)

try:
    opts, args = getopt.getopt(sys.argv[1:], "in:")
except getopt.GetoptError as e:
    print(e.msg)
    usage()

infile = open(args[0]) if args else sys.stdin
while True:
    l = infile.readline()
    if l == "": break
    sub = l[60: 65]
    if(sub.strip() == ""):
        l = l[:60] + '0' + l[60:]
    result = re.sub('  +',',',l)
    with open('data.csv', 'a') as the_file:
        the_file.write(result)

