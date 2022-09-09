import requests
import key
import csv
from opensecrets_api import OpenSecrets
from pprint import pprint
import pickle
from candidate import Candidate


cid_list = []

with open('/Users/timmy the man/Desktop/Project VoteSmart/subset_file.csv',  encoding='utf-8-sig') as f:
    csv_file_data = csv.reader(f)
    for row in csv_file_data:
        cid_list.append(row[0])

o = OpenSecrets(key.API_KEY)


candidates = []

for cid in cid_list:
    raw_data = {}
    for cycle in ['2012', '2014', '2016', '2018', '2020', '2022']:
        try:
            api_result = o.get_candidate_summary(cid, cycle=cycle)
            raw_data[cycle] = api_result
            print("appending data " + cid + ' '+cycle)

        except TypeError:
            print("Not found " + cid)

        pprint(raw_data)

    try:
        candidate = Candidate(cid=cid,
                              name=raw_data['2022']['cand_name'],
                              cycle=raw_data.keys(),
                              state=raw_data['2022']['state'],
                              party=raw_data['2022']['party'],
                              chamber=raw_data['2022']['chamber'])

        candidates.append(candidate)

    except KeyError:
        pass


for candidate in candidates:
    pprint(candidate)


with open('my_practice_pickled_file', 'wb') as f:
    pickle.dump(candidates, f)
