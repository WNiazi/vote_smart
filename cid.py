import requests
import key
import csv
from opensecrets_api import OpenSecrets
from pprint import pprint

cid_list = []

with open('/Users/timmy the man/Desktop/Project VoteSmart/filtered_all_candiate.csv',  encoding='utf-8-sig') as f:
    csv_file_data = csv.reader(f)
    for row in csv_file_data:
        cid_list.append(row[0])

pprint(cid_list)

# for row_cid in csv_file_data:
#    cid = row_cid[0]
#    print(cid)
#    cid_list.append(cid)


o = OpenSecrets(key.API_KEY)
# by_cid = o.get_legislators(  # need cid)
