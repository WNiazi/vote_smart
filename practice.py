from xml.sax.xmlreader import AttributesImpl
import requests
import key
import csv
from opensecrets_api import OpenSecrets
from pprint import pprint
import pickle
from candidate import Candidate
from contribution import Contribution


cid_list = []

with open('/Users/timmy the man/Desktop/Project VoteSmart/subset_file.csv',  encoding='utf-8-sig') as f:
    csv_file_data = csv.reader(f)
    for row in csv_file_data:
        cid_list.append(row[0])

o = OpenSecrets(key.API_KEY)


candidates = []
cycles = ['2022', '2020', '2018', '2016', '2014', '2012']

for cid in cid_list:
    raw_data = {}
    for cycle in cycles:
        try:
            api_result = o.get_candidate_summary(cid, cycle=cycle)
            cand_contribution = o.get_candidate_contributors(cid, cycle=cycle)
            contributors = cand_contribution[0]
            # print(contributors)  # -this will get us all the Attributes
            contributions_list = []
            for each_contributors in contributors:
                contributions_list.append(each_contributors['@attributes'])

            # print(contributions_list)
# [{'org_name': 'Butler Toyota', 'total': '10000', 'pacs': '0', 'indivs': '10000'}, {'org_name': 'Citizens United', 'total': '10000', 'pacs': '10000', 'indivs': '0'}, {'org_name': 'IDT Corp', 'total': '8250', 'pacs': '5000', 'indivs': '3250'}, {'org_name': 'Bank of S E Europe', 'total': '5000', 'pacs': '0', 'indivs': '5000'}, {'org_name': 'Corp Travel Coordinators of Americ', 'total': '5000', 'pacs': '0', 'indivs': '5000'}, {
#    'org_name': 'Credit Union National Assn', 'total': '5000', 'pacs': '5000', 'indivs': '0'}, {'org_name': 'Del Mar Country Club', 'total': '5000', 'pacs': '0', 'indivs': '5000'}, {'org_name': 'Ecolab Inc', 'total': '5000', 'pacs': '5000', 'indivs': '0'}, {'org_name': 'Humane Society Legislative Fund', 'total': '5000', 'pacs': '5000', 'indivs': '0'}, {'org_name': 'Independent Insurance Agents & Brokers of America', 'total': '5000', 'pacs': '5000', 'indivs': '0'}]

            #[{'@attributes': {'org_name': 'Butler Toyota', 'total': '10000', 'pacs': '0', 'indivs': '10000'}}, {'@attributes': {'org_name': 'Citizens United', 'total': '10000', 'pacs': '10000', 'indivs': '0'}}, {'@attributes': {'org_name': 'IDT Corp', 'total': '8250', 'pacs': '5000', 'indivs': '3250'}}, {'@attributes': {'org_name': 'Bank of S E Europe', 'total': '5000', 'pacs': '0', 'indivs': '5000'}}, {'@attributes': {'org_name': 'Corp Travel Coordinators of Americ', 'total': '5000', 'pacs': '0', 'indivs': '5000'}}, {'@attributes': {'org_name': 'Credit Union National Assn', 'total': '5000', 'pacs': '5000', 'indivs': '0'}}, {'@attributes': {'org_name': 'Del Mar Country Club', 'total': '5000', 'pacs': '0', 'indivs': '5000'}}, {'@attributes': {'org_name': 'Ecolab Inc', 'total': '5000', 'pacs': '5000', 'indivs': '0'}}, {'@attributes': {'org_name': 'Humane Society Legislative Fund', 'total': '5000', 'pacs': '5000', 'indivs': '0'}}, {'@attributes': {'org_name': 'Independent Insurance Agents & Brokers of America', 'total': '5000', 'pacs': '5000', 'indivs': '0'}}]
# {'cand_name': 'Dan Burton (R)', 'cid': 'N00000010', 'cycle': '2012', 'origin': 'Center for Responsive Politics', 'source': 'https://www.opensecrets.org/members-of-congress/contributors?cid=N00000010&cycle=2012',
 # 'notice': "The organizations themselves did not donate, rather the money came from the organization's PAC, its individual members or employees or owners, and those individuals' immediate families."}

            #raw_data[cycle] = api_result
            #raw_data[cycle]['contributions'] = cand_contribution
            #print("appending data " + cid + ' '+cycle)

        except TypeError:
            print("Not found " + cid)

        pprint(raw_data)

    # Name: most recent
    name = None
    for cycle in cycles:
        try:
            name = raw_data[cycle]['cand_name']

        except KeyError:
            print("Name not found in " + cycle + " cycle")
        if name:
            break
    if name:
        print("Name: " + name)

    # State: list of all states
    state = []
    for cycle in cycles:
        try:
            state_per_cycle = raw_data[cycle]['state']
        except KeyError:
            print("no state found in the " + cycle + " cycle")
            continue
        state.append(state_per_cycle)

    # Party: dictionary Year/Party
    party = {}
    for cycle in cycles:
        try:
            party_per_cycle = raw_data[cycle]['party']
        except KeyError:
            print("no party found in the " + cycle + " cycle")
            continue
        party[cycle] = party_per_cycle

    # chamber: dictionary Year/Chamber
    chamber = {}
    for cycle in cycles:
        try:
            chamber_per_cycle = raw_data[cycle]['chamber']
        except KeyError:
            print("no chamber found in the " + cycle + " cycle")
            continue
        chamber[cycle] = chamber_per_cycle

    # contributions: dictionary of lists, per cycle
 #   contributions = {}
#    for cycle in cycles:
 #       contributions_per_cycle = []
 #       try:
  #          raw_contributions_per_cycle = raw_data[cycle]['contributions']
   #         raw_contributions_per_cycle = [
  #              x for x in raw_contributions_per_cycle if '@attributes' in x]
  #          print(type(raw_contributions_per_cycle))
   #         pprint(raw_contributions_per_cycle)
#
 #           for contribution in raw_contributions_per_cycle:
   #             org_name = contribution['@attributes']['org_name']
  #              total = contribution['@attributes']['total']
   #             pacs = contribution['@attributes']['pacs']
   #             indivs = contribution['@attributes']['indivs']

   #             contributions_per_cycle.append(Contribution(
    #                org_name=org_name, total=total, pacs=pacs, individual=indivs))

          #  except KeyError:
           #     print("no contributions found in the " + cycle + " cycle")
            #    continue
    #    contributions[cycle] = contributions_per_cycle

    candidate = Candidate(cid=cid,
                          name=name,
                          cycle=list(raw_data.keys()),
                          state=state,  # List
                          party=party,
                          chamber=chamber)

    candidates.append(candidate)


for candidate in candidates:
    pprint(candidate)


with open('my_practice_pickled_file', 'wb') as f:
    pickle.dump(candidates, f)
