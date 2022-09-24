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
        except TypeError:
            print("Not found " + cid)

        # pprint(raw_data)

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
    contributions = {}
    for cycle in cycles:
        contributions_per_cycle = []
        try:
            cand_contribution = o.get_candidate_contributors(cid, cycle=cycle)
            raw_contributions_per_cycle = cand_contribution[0]
           # pprint(type(raw_contributions_per_cycle))
            org_name = raw_contributions_per_cycle['@attributes']['org_name']
            # print(org_name)
            total = raw_contributions_per_cycle['@attributes']['total']
            # print(total)
            pacs = raw_contributions_per_cycle['@attributes']['pacs']
            # print(pacs)
            individual = raw_contributions_per_cycle['@attributes']['indivs']
            # print(individual)

        except KeyError:
            print("no contributions found in the " + cycle + " cycle")
            continue

        # contributions.update(contributions_per_cycle)
    contributions_per_cycle = Contribution(
        org_name=org_name, total=total, pacs=pacs, individual=individual)
    pprint(contributions_per_cycle)

    candidate = Candidate(cid=cid,
                          name=name,
                          cycle=list(raw_data.keys()),
                          state=state,  # List
                          party=party,
                          chamber=chamber)

    candidates.append(candidate)


for candidate in candidates:
    pprint(candidate)

for each_contribution in contributions:
    pprint(each_contribution)

with open('my_practice_pickled_file', 'wb') as f:
    pickle.dump(candidates, f)
