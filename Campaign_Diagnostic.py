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


#Turn csv into a JSON object

csv_sc_df = open('C:\Users\Jonathan\Downloads\KV Report, Account hothead_04, 2015-07-15 - 2015-08-14.csv')
json_sc_df = open("C:\Users\Jonathan\Downloads\KV Report, Account hothead_04, 2015-07-15 - 2015-08-14.json","w+")


fieldnames = ('\xef\xbb\xbf"Reporting Starts',"Reporting Ends","Campaign Name","Ad Set Name","Ad Name","Impressions","Amount Spent (USD)","Clicks","Gender","Age","Website Clicks [28 Days After Clicking]","Ad Set ID","Campaign ID","Mobile App Installs [28 Days After Clicking]","Ad ID")
reader=csv.DictReader(csv_sc_df,fieldnames)

#count the number of rows in the csv
csv_count = 0
for row in reader:
    #print row
    json.dump(row, json_sc_df)
    json_sc_df.write('\n')
    csv_count+=1
print csv_count, "the number of rows convereted from the csv into JSON"

json_data=(json_sc_df).read()
json_sc = json.loads(json_data)
print json_sc



#Get a list of every column header
#column_names=[]
#for column in sc_df:
 #   column_names.append(column)
#print column_names

#Filtering by campaign ids

#1:1:1
#find out the unique campaign ids
# all_campaign_ids = []
# count = 0
# unique_campaign_ids = []
# total_count=0
# for row in sc_df['Campaign ID']:
#     total_count+=1
#     if row not in unique_campaign_ids:
#         unique_campaign_ids.append(row)
#         count +=1
#     else:
#         all_campaign_ids.append(row)
#
# print unique_campaign_ids
# print "count", count
# print "total campaign count",total_count
#
# #Next, match up individual ad set ids to these campaign ids
#



