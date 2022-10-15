import key
import csv
from opensecrets_api import OpenSecrets
from pprint import pprint
import practice_contribute


o = OpenSecrets(key.API_KEY)

sorted = practice_contribute.org_name_list
print(sorted)


get_organization = o.get_organizations('Brett Robinson Real Estate')
# print(get_organization){'@attributes': {'orgid': 'D000092409', 'orgname': 'Brett Robinson Real Estate'}}
get_organization_summary = o.get_organization_summary('D000092409')
# print(get_organization_summary)
#{'cycle': '2022', 'orgid': 'D000092409', 'orgname': 'Brett Robinson Real Estate', 'total': '60065', 'indivs': '60065', 'pacs': '0', 'soft': '0', 'tot527': '0', 'dems': '2915', 'repubs': '57150', 'lobbying': '0', 'outside': '0', 'mems_invested': '0', 'gave_to_pac': '0', 'gave_to_party': '0', 'gave_to_527': '0', 'gave_to_cand': '49325', 'source': 'www.opensecrets.org/orgs/summary.php?id=D000092409'}
