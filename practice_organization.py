import key
from opensecrets_api import OpenSecrets
from pprint import pprint
from organization import Organization
import csv
import organization


o = OpenSecrets(key.API_KEY)

listoforg = []
with open('contribs.csv',  encoding='utf-8-sig') as f:
    csv_file_data = csv.reader(f)
    for row in csv_file_data:
        listoforg.append(row[3])

listoforg = list(set(listoforg))

data = []
orgid = []
total_organization = []
for each_org in listoforg:
    try:
        org = o.get_organizations(each_org)
        data.append(org)
        # print(data)
    except TypeError:
        print("Not found " + each_org)


for each_data in data:
    if not isinstance(each_data, list):
        each_data = [each_data]
    for indiv_data in each_data:
        inform_att = indiv_data.get('@attributes')
        inform_id = inform_att.get('orgid')
        orgid.append(inform_id)

# print(orgid)

for each_orgid in orgid:
    infor_about_each_org = o.get_organization_summary(each_orgid)

    organization = Organization(organizations=infor_about_each_org)

    total_organization.append(organization)

# pprint(total_organization)

cvsheader = ['CYCLE', 'ORGID', 'ORGNAME', 'TOTAL', 'INDIVS', 'PACS', 'SOFT', 'TOT527', 'DEMS', 'REPUBS',
             'LOBBYING', 'OUTSIDE', 'MEMS_INVESTED', 'GAVE_TO_PAC', 'GAVE_TO_PARTY', 'GAVE_TO_527', 'GAVE_TO_CAND', 'SOURCE']
# write mode =w; # file object =f , creating new object

with open('organs.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(cvsheader)
    for org in total_organization:
        writer.writerow(org.get_organization_row())
