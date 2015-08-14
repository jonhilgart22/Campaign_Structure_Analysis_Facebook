__author__ = 'Jonathan'

#initial imports

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import Series,DataFrame
import json
import csv

print "Hello World"


#Intial commit to turn the JSON into a Dataframe
#df = pd.read_json('api url to hit and get back data')

sc_df = pd.read_csv('C:\Users\Jonathan\Downloads\KV Report, Account hothead_04, 2015-07-15 - 2015-08-14.csv')

#Get a list of every column header
column_names=[]
for column in sc_df:
    column_names.append(column)
print column_names

#Filtering by campaign ids

#1:1:1
#find out the unique campaign ids
unique_campaign_ids = []
all_campaign_ids = []
count = 0
total_count=0
for row in sc_df['Campaign ID']:
    total_count+=1
    if row not in unique_campaign_ids:
        unique_campaign_ids.append(row)
        count +=1
    else:
        all_campaign_ids.append(row)

print unique_campaign_ids
print "count", count
print "total campaign count",total_count

#Next, match up individual ad set ids to these campaign ids




