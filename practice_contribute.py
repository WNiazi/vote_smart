import key
import csv
from opensecrets_api import OpenSecrets
from pprint import pprint
from contribution import Contribution


cid_list = []

with open('/Users/timmy the man/Desktop/Project VoteSmart/subset_file.csv',  encoding='utf-8-sig') as f:
    csv_file_data = csv.reader(f)
    for row in csv_file_data:
        cid_list.append(row[0])


o = OpenSecrets(key.API_KEY)


total_cand_contribution_information = []
cycles = ['2022', '2020', '2018', '2016', '2014', '2012']
information_dict_candidate = {}

org_name_list = []

for cid in cid_list:
    raw_data = {}
    for cycle in cycles:
        try:
            cand_contribution = o.get_candidate_contributors(cid, cycle=cycle)
            raw_data[cycle] = cand_contribution
        except TypeError:
            print("not found " + cid)
    # pprint(raw_data)

    atts_list = []
    for cycle in cycles:
        try:
            (contribution_list, stuff) = raw_data[cycle]
            if not isinstance(contribution_list, list):
                contribution_list = [contribution_list]

            for for_atts in contribution_list:
                att = for_atts.get('@attributes')
                att_org_name = att.get('org_name')
                att['cycle'] = cycle
                atts_list.append(att)
                org_name_list.append(att_org_name)

            contribution = Contribution(
                cid=cid, cycle=cycle, contributions=atts_list)

            total_cand_contribution_information.append(contribution)

        except KeyError:
            print("no contributions was found " + cid + " " + cycle + " cycle")


cvsheader = ['CID', 'CYCLE', 'NAME', 'INDVIS',
             'ORG_NAME', 'PACS', 'TOTAL', 'SOURCE']
# write mode =w; # file object =f , creating new object

with open('contrib.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(cvsheader)
    for con in total_cand_contribution_information:
        con_rows = con.get_contribution_rows()
        for row in con_rows:
            writer.writerow(row)

f.close()
