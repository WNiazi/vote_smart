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
            raw_data[cycle] = api_result
        except TypeError:
            print("Not found " + cid)

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


# Candidate(cid=N00000010, name=Burton, Dan, cycle=['2022', '2020', '2018', '2016', '2014', '2012'], state=['', '', '', '', '', 'IN'], party={'2022': 'R', '2020': 'R', '2018': 'R', '2016': 'R', '2014': 'R', '2012': 'R'}, chamber={'2022': '', '2020': '', '2018': '', '2016': '', '2014': '', '2012': 'H'})
#Candidate(cid=N00000011, name=None, cycle=[], state=[], party={}, chamber={})
# Candidate(cid=N00000019, name=Clinton, Hillary, cycle=['2022', '2020', '2018', '2016', '2014', '2012'], state=['', '', '', 'NY', '', ''], party={'2022': 'D', '2020': 'D', '2018': 'D', '2016': 'D', '2014': 'D', '2012': 'D'}, chamber={'2022': '', '2020': '', '2018': '', '2016': 'Pres', '2014': '', '2012': ''})
# Candidate(cid=N00000036, name=Feingold, Russ, cycle=['2020', '2018', '2016', '2014', '2012'], state=['', '', '', '', ''], party={'2020': 'D', '2018': 'D', '2016': 'D', '2014': 'D', '2012': 'D'}, chamber={'2020': '', '2018': '', '2016': '', '2014': '', '2012': ''})
