# -*- coding: utf-8 -*-
from pprint import pprint 
import pandas

csv = pandas.read_csv("./pinYinTable.csv", encoding='utf-16-le')
pprint(csv)
