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


cycles = ['2022', '2020', '2018', '2016', '2014', '2012']
raw_data = {}
almost_final_contributions = []

for cid in cid_list:
    for cycle in cycles:
        try:
            cand_contribution = o.get_candidate_contributors(cid, cycle=cycle)
            raw_data[cycle] = cand_contribution
        except TypeError:
            print("not found " + cid)

# raw_data = {'2022': ({'@attributes': {'org_name': 'General Dynamics', 'total': '0', 'pacs': '0', 'indivs': '0'}}, {'cand_name': 'Dan Burton (R)', 'cid': 'N00000010', 'cycle': '2022', 'origin': 'Center for Responsive Politics', 'source': 'https://www.opensecrets.org/members-of-congress/contributors?cid=N00000010&cycle=2022', 'notice': "The organizations themselves did not donate, rather the money came from the organization's PAC, its individual members or employees or owners, and those individuals' immediate families."}), '2020': ([{'@attributes': {'org_name': 'Adtalem Global Education', 'total': '0', 'pacs': '0', 'indivs': '0'}}, {'@attributes': {'org_name': 'American Soybean Assn', 'total': '0', 'pacs': '0', 'indivs': '0'}}, {'@attributes': {'org_name': 'Auto Care Assn', 'total': '0', 'pacs': '0', 'indivs': '0'}}, {'@attributes': {'org_name': 'DTE Energy', 'total': '0', 'pacs': '0', 'indivs': '0'}}, {'@attributes': {'org_name': 'General Dynamics', 'total': '0', 'pacs': '0', 'indivs': '0'}}, {'@attributes': {'org_name': 'National Turkey Federation', 'total': '0', 'pacs': '0', 'indivs': '0'}}, {'@attributes': {'org_name': 'Solar Energy Industries Assn', 'total': '0', 'pacs': '0', 'indivs': '0'}}], {'cand_name': 'Dan Burton (R)', 'cid': 'N00000010', 'cycle': '2020', 'origin': 'Center for Responsive Politics', 'source': 'https://www.opensecrets.org/members-of-congress/contributors?cid=N00000010&cycle=2020', 'notice': "The organizations themselves did not donate, rather the money came from the organization's PAC, its individual members or employees or owners, and those individuals' immediate families."}), '2012': (
 #   [{'@attributes': {'org_name': 'Butler Toyota', 'total': '10000', 'pacs': '0', 'indivs': '10000'}}, {'@attributes': {'org_name': 'Citizens United', 'total': '10000', 'pacs': '10000', 'indivs': '0'}}, {'@attributes': {'org_name': 'IDT Corp', 'total': '8250', 'pacs': '5000', 'indivs': '3250'}}, {'@attributes': {'org_name': 'Bank of S E Europe', 'total': '5000', 'pacs': '0', 'indivs': '5000'}}, {'@attributes': {'org_name': 'Corp Travel Coordinators of Americ', 'total': '5000', 'pacs': '0', 'indivs': '5000'}}, {'@attributes': {'org_name': 'Credit Union National Assn', 'total': '5000', 'pacs': '5000', 'indivs': '0'}}, {'@attributes': {'org_name': 'Del Mar Country Club', 'total': '5000', 'pacs': '0', 'indivs': '5000'}}, {'@attributes': {'org_name': 'Ecolab Inc', 'total': '5000', 'pacs': '5000', 'indivs': '0'}}, {'@attributes': {'org_name': 'Humane Society Legislative Fund', 'total': '5000', 'pacs': '5000', 'indivs': '0'}}, {'@attributes': {'org_name': 'Independent Insurance Agents & Brokers of America', 'total': '5000', 'pacs': '5000', 'indivs': '0'}}], {'cand_name': 'Dan Burton (R)', 'cid': 'N00000010', 'cycle': '2012', 'origin': 'Center for Responsive Politics', 'source': 'https://www.opensecrets.org/members-of-congress/contributors?cid=N00000010&cycle=2012', 'notice': "The organizations themselves did not donate, rather the money came from the organization's PAC, its individual members or employees or owners, and those individuals' immediate families."})}

    org_name = []
    total = []
    pacs = []
    indiv = []
    for cycle in cycles:
        try:
            index_contribution = raw_data[cycle][0]
            index = 0
            while index < len(index_contribution):
                for key in index_contribution[index]:
                    information = index_contribution[index][key]
                    org_name_per_cycle = information['org_name']
                    total_per_cycle = information['total']
                    pacs_per_cycle = information['pacs']
                    indivs_per_cycle = information['indivs']
                index += 1

        except KeyError:
            print("nothing was found is not found in " + cycle + " cycle")
            continue
        org_name.append(org_name_per_cycle)
        total.append(total_per_cycle)
        pacs.append(pacs_per_cycle)
        indiv.append(indivs_per_cycle)

    contributions = Contribution(cid=cid,
                                 cycle=list(raw_data.keys()),
                                 org_name=org_name,
                                 total=total,
                                 individual=indiv,
                                 pacs=pacs)

    almost_final_contributions.append(contributions)

    for contribution in almost_final_contributions:
        pprint(contribution)

# NOT THE CORRECTION INFORMATION BUT CAN MAKE CLASSES?

# Contribution(cid=N00000010, org_name=['Solar Energy Industries Assn', 'Independent Insurance Agents & Brokers of America'], total=[
       #      '0', '5000'], pac=['0', '5000'], individual=['0', '0'])
# Contribution(cid=N00000011, org_name=['Solar Energy Industries Assn', 'Independent Insurance Agents & Brokers of America'], total=[
  #           '0', '5000'], pac=['0', '5000'], individual=['0', '0'])
# Contribution(cid=N00000019, org_name=['Solar Energy Industries Assn', 'Irish American Democrats', 'Independent Insurance Agents & Brokers of America'], total=[
      #       '0', '1000', '5000'], pac=['0', '1000', '5000'], individual=['0', '0', '0'])
# Contribution(cid=N00000036, org_name=['Solar Energy Industries Assn', 'Korein Tillery LLC', 'Independent Insurance Agents & Brokers of America'], total=[
        #   '0', '43200', '5000'], pac=['0', '0', '5000'], individual=['0', '43200', '0'])
# Contribution(cid=N00000039, org_name=['Solar Energy Industries Assn', 'Korein Tillery LLC', 'Independent Insurance Agents & Brokers of America'], total=[
        #   '0', '43200', '5000'], pac=['0', '0', '5000'], individual=['0', '43200', '0'])


# DanBurtonN00000010
#([{'@attributes': {'org_name': 'Adtalem Global Education', 'total': '0', 'pacs': '0', 'indivs': '0'}}, {'@attributes': {'org_name': 'American Soybean Assn', 'total': '0', 'pacs': '0', 'indivs': '0'}}, {'@attributes': {'org_name': 'Auto Care Assn', 'total': '0', 'pacs': '0', 'indivs': '0'}}, {'@attributes': {'org_name': 'DTE Energy', 'total': '0', 'pacs': '0', 'indivs': '0'}}, {'@attributes': {'org_name': 'General Dynamics', 'total': '0', 'pacs': '0', 'indivs': '0'}}, {'@attributes': {'org_name': 'National Turkey Federation', 'total': '0','pacs': '0', 'indivs': '0'}}, {'@attributes': {'org_name': 'Solar Energy Industries Assn', 'total': '0', 'pacs': '0', 'indivs': '0'}}], {'cand_name': 'Dan Burton (R)', 'cid': 'N00000010', 'cycle': '2020', 'origin': 'Center for Responsive Politics', 'source': 'https://www.opensecrets.org/members-of-congress/contributors?cid=N00000010&cycle=2020', 'notice': "The organizations themselves did not donate, rather the money came from the organization's PAC, its individual members or employees or owners, and those individuals' immediate families."})
#get_organizations = o.get_organizations('Brett Robinson Real Estate')
# print(get_organizations){'@attributes': {'orgid': 'D000092409', 'orgname': 'Brett Robinson Real Estate'}}
