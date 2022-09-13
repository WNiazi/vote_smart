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
            raw_data[cycle] = api_result
            raw_data[cycle]['contributions'] = cand_contribution
            print("appending data " + cid + ' '+cycle)

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

    # contirbutions: dictionary of lists, per cycle
    contributions = {}
    for cycle in cycles:
        contributions_per_cycle = []
        try:
            raw_contributions_per_cycle = raw_data[cycle]['contributions']
            raw_contributions_per_cycle = [
                x for x in raw_contributions_per_cycle if '@attributes' in x]
            print(type(raw_contributions_per_cycle))
            pprint(raw_contributions_per_cycle)

            for contribution in raw_contributions_per_cycle:
                org_name = contribution['@attributes']['org_name']
                total = contribution['@attributes']['total']
                pacs = contribution['@attributes']['pacs']
                indivs = contribution['@attributes']['indivs']

                contributions_per_cycle.append(Contribution(
                    org_name=org_name, total=total, pacs=pacs, individual=indivs))

        except KeyError:
            print("no contributions found in the " + cycle + " cycle")
            continue
        contributions[cycle] = contributions_per_cycle

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
