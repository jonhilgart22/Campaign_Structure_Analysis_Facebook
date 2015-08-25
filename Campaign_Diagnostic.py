__author__ = 'Jonathan'

#initial imports

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import Series,DataFrame
import json
import csvkit

print "Hello World"


#Turn csv into a JSON object

hh_04 = pd.read_json('C:\Users\Jonathan\Downloads\convertcsv.json')
print hh_04.head()



#Get a list of every column header
column_names=[]
for column in hh_04:
   column_names.append(column)
print column_names


#Filtering by campaign ids

#find out the unique campaign ids


all_campaign_ids = []
count = 0
unique_campaign_ids = []
total_count=0
for row in hh_04['Campaign ID']:
    total_count+=1
    if row not in unique_campaign_ids:
        unique_campaign_ids.append(row)
        count +=1
    else:
        all_campaign_ids.append(row)

print unique_campaign_ids
print "unique campaign count", count
print "total campaign count",total_count



#Next, match up individual ad set ids to these campaign ids


unique_ad_set_ids = []
all_ad_set_ids=[]
count_of_unique_ad_sets = 0
total_ad_sets = 0
for row in hh_04['Ad Set ID']:
    total_ad_sets +=1
    if row not in unique_ad_set_ids:
        unique_ad_set_ids.append(row)
        count_of_unique_ad_sets+=1
    else:
        all_ad_set_ids.append(row)
print "count of unique ad sets",count_of_unique_ad_sets
print "count of total ad sets", total_ad_sets

#find ad sets for each unique campaign id, campaign id combined with ad id
campaign_ad_set_combo = {}

for campaign_id in unique_campaign_ids:
    campaign_ad_set_combo.setdefault(campaign_id,[])
    for ad_set_id in unique_ad_set_ids:
        campaign_ad_set_combo[campaign_id].append(ad_set_id)
        #print campaign_id,"campaignid"
        #print ad_id,"ad id"
print campaign_ad_set_combo
print campaign_ad_set_combo.keys() ,"campaign ad set keys"
campaign_ad_set_combo = DataFrame(campaign_ad_set_combo)
print campaign_ad_set_combo.head() , "data frame ad set combo"


#Now, find the unique ads

unique_ad_ids = []
count_ad_ids = 0

for row in hh_04['Ad ID']:
    if row not in unique_ad_ids:
        unique_ad_ids.append(row)
        count_ad_ids +=1
print count_ad_ids, "total number of ads"

#Match ads with each ad set

ad_set_id_ad_id_combo = {}

for ad_set_id in unique_ad_set_ids:
    ad_set_id_ad_id_combo.setdefault(ad_set_id,[])
    for ad_id in unique_ad_ids:
        ad_set_id_ad_id_combo[ad_set_id].append(ad_id)

print ad_set_id_ad_id_combo,\"ad set id combo"



