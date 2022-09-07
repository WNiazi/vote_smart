import requests
import key
import csv
from opensecrets_api import OpenSecrets
from pprint import pprint
import pickle


cid_list = []

with open('/Users/timmy the man/Desktop/Project VoteSmart/subset_file.csv',  encoding='utf-8-sig') as f:
    csv_file_data = csv.reader(f)
    for row in csv_file_data:
        cid_list.append(row[0])

o = OpenSecrets(key.API_KEY)


cid_cycle_data = {}

for cycle in ['2012', '2014', '2016', '2018', '2020', '2022', '']:
    for cid in cid_list:
        try:
            cand_infor = o.get_candidate_summary(cid, cycle=cycle)
            cand_contributors = o.get_candidate_contributors(cid, cycle=cycle)
            if cid not in cid_cycle_data:
                cid_cycle_data[cid] = None
            print("appending data")
            cid_cycle_data[cid][cycle] = cand_infor

        except:
            print("Not found " + cid)
            #not_found_cid.append (each_cid)
pprint(cid_cycle_data)


with open('my_practice_pickled_file', 'wb') as f:
    pickle.dump(cid_cycle_data, f)
