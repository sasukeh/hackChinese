# -*- coding: utf-8 -*-
from pprint import pprint 
import re
import csv
import os

# pathObjectToJson
def jsonFileToDict(file):
  f = open(file)
  return json.load(f)

def csvFileToCsvObject(file, readerType=""):
  f = open(file, encoding='utf_8_sig' ) 
  if readerType=="dict":
    return csv.DictReader(f)
  else:
    return csv.reader(f)


