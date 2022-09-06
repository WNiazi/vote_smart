import requests
import key
import csv
from opensecrets_api import OpenSecrets
from pprint import pprint
import unicodedata

cid_list = []

with open('/Users/timmy the man/Desktop/Project VoteSmart/filtered_all_candiate.csv',  encoding='utf-8-sig') as f:
    csv_file_data = csv.reader(f)
    for row in csv_file_data:
        cid_list.append(row[0])


o = OpenSecrets(key.API_KEY)

for each_cid in cid_list:
    pprint(o.get_legislators(each_cid))
