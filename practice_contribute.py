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

raw_data = {}
almost_final_contributions = []
org_name = []
total_cand_contribution_information = []
information_per_year_candidate = []
cycles = ['2022', '2020', '2018', '2016', '2014', '2012']
for cid in cid_list:
    for cycle in cycles:
        try:
            cand_contribution = o.get_candidate_contributors(cid, cycle=cycle)
            raw_data[cycle] = cand_contribution
        except TypeError:
            print("not found " + cid)
   # information_dict_candidate = {}
    for cycle in cycles:
        try:
            index_contribution = raw_data[cycle][0]
            index = 0
            while index < len(index_contribution):
                for key in index_contribution[index]:
                    information_per_candidate = index_contribution[index][key]
                    #information_dict_candidate[cycle] = information_per_candidate

                    org_name_per_cycle = information_per_candidate['org_name']
                    information_per_year_candidate.append(
                        information_per_candidate)
                    index += 1
        except KeyError:
            print("no contributions was found " + cid + " " + cycle + " cycle")
            continue
       # org_name.append(org_names)
        total_cand_contribution_information.append(
            information_per_year_candidate)
        # print(total_cand_contribution_information)


contributions = Contribution(cid=cid, cycle=list(
    raw_data.keys()), org_name=org_name, information=total_cand_contribution_information)

almost_final_contributions.append(contributions)

# for contribution in almost_final_contributions:
#   pprint(contribution)

#Issue now is the Class Contribution is not providing cycle/cid numbers #
