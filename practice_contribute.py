from xml.sax.xmlreader import AttributesImpl
import requests
import key
import csv
from opensecrets_api import OpenSecrets
from pprint import pprint
import pickle
from candidate import Candidate
from contribution import Contribution
import pandas as pd


cid_list = []

with open('/Users/timmy the man/Desktop/Project VoteSmart/subset_file.csv',  encoding='utf-8-sig') as f:
    csv_file_data = csv.reader(f)
    for row in csv_file_data:
        cid_list.append(row[0])

o = OpenSecrets(key.API_KEY)


contribution_candidate = []
cycles = ['2022', '2020', '2018', '2016', '2014', '2012']
raw_data = []
for cid in cid_list:

    for cycle in cycles:
        try:
            cand_contribution = o.get_candidate_contributors(cid, cycle=cycle)
            # pprint(cand_contribution)

            #candidates_info = cand_contribution[1]
            # pprint(candidates_info)
            #cand_cid = candidates_info['cid']
            # raw_data.append(cand_cid)

            # print(raw_data)

            index_contribution = cand_contribution[0]
            # pprint(index_contribution)

            for contribution_per_cand in index_contribution:
                org_name = contribution_per_cand['@attributes']['org_name']
                total = contribution_per_cand['@attributes']['total']
                pacs = contribution_per_cand['@attributes']['pacs']
                indivs = contribution_per_cand['@attributes']['indivs']

            raw_data.append(Contribution(org_name=org_name,
                                         total=total, pacs=pacs, individual=indivs))
            # pprint(raw_data)
            # [Contribution(org_name=Service Employees International Union, total=15000, pac=15000, individual=0),
            # Contribution(org_name=American Assn for Justice, total=15000, pac=15000, individual=0)]

        except TypeError:
            print("Not found " + cid)

pprint(raw_data)
# []

cvsheader = ['ORGNAME', 'TOTAL', 'PACS', 'INDIV']

with open('contribution_final.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(cvsheader)

    writer.writerow(raw_data[Contribution])


# pickling (store object in binary); wb is write binary
# with open('my_practice_pickled_contribution_file', 'wb') as f:
#  pickle.dump(raw_data, f)
# f.close()

# unpickling/deserialization returns to python object; read binary =rb
#unpic = open( 'rb')
#raw_data = pickle.load(unpic)
# print(raw_data)
# unpic.close()
