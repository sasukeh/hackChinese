# -*- coding: utf-8 -*-
from pprint import pprint 
import csv

def csvFileToCsvObject(file, readerType=""):
  f = open(file, "r") 
  if readerType=="dict":
    return csv.DictReader(f)
  else:
    return csv.reader(f)

csv = csvFileToCsvObject("./pinYinTable.csv")
# for a in tsv:
#   pprint(a)
for a in csv:
  pprint(a)

