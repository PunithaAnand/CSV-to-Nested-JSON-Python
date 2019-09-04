# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:05:45 2019

@author: Punitha
"""

from csv import DictReader
from itertools import groupby
from pprint import pprint
import json
#Open the input CSV file 

with open(r'C:\Sample1.csv') as csvfile:
    r = DictReader(csvfile, skipinitialspace=True)
    data = [dict(d) for d in r]

    groups = []
    uniquekeys = []
#
    for k, g in groupby(data, lambda r: (r['JobID'], r['JobDate'],r['JobTitle'],r['Division'],r['State'])):
        groups.append({
            "JobId": k[0],
            "JobDate": k[1],
            "JobTitle":k[2],
            "Division":k[3],
            "State":k[4],
            "Skills": [{k:v for k, v in d.items() if k not in ['JobID','JobDate','JobTitle','Division','State']} for d in list(g)]
        })
        uniquekeys.append(k)

pprint(groups)
#Specify the path of output file name to store JSON objects
with open('Jobs.json', 'w') as outfile:
    json.dump(groups, outfile)