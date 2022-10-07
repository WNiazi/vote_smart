class Contribution:
    def __init__(self, cid, cycle, org_name, information, source='https://www.opensecrets.org'):
        self.cid = cid
        self.cycle = cycle
        self.org_name = org_name
        self.information = information
        self.source = source

    def __str__(self) -> str:
        if self.org_name:
            return self.org_name
        else:
            return "Unknown"

    def __repr__(self) -> str:
        return "Contribution(cid ={}, org_name={}, information={})".format(self.cid, self.org_name, self.information)


#cand_contribution = o.get_candidate_contributors('N00044245')
# print(cand_contribution)
#([{'@attributes': {'org_name': 'Brett Robinson Real Estate', 'total': '24970', 'pacs': '0', 'indivs': '24970'}}, {'@attributes': {'org_name': 'Burton Property Group', 'total': '21000', 'pacs': '0', 'indivs': '21000'}}, {'@attributes': {'org_name': 'Esfeller Construction', 'total': '20900', 'pacs': '0', 'indivs': '20900'}}, {'@attributes': {'org_name': 'Core Industries', 'total': '17875', 'pacs': '0', 'indivs': '17875'}}, {'@attributes': {'org_name': 'Encore Rehabilitation', 'total': '16800', 'pacs': '0', 'indivs': '16800'}}, {'@attributes': {'org_name': 'Eye of the Tiger PAC', 'total': '15000', 'pacs': '15000', 'indivs': '0'}}, {'@attributes': {'org_name': 'Majority Cmte PAC', 'total': '15000', 'pacs': '15000','indivs': '0'}}, {'@attributes': {'org_name': 'Southern Co', 'total': '15000', 'pacs': '15000', 'indivs': '0'}}, {'@attributes': {'org_name': 'Volkert Inc', 'total': '15000', 'pacs': '15000', 'indivs': '0'}}, {'@attributes': {'org_name': 'Lafayette Land Co', 'total': '13200', 'pacs': '0', 'indivs': '13200'}}], {'cand_name': 'Jerry Carl (R)', 'cid': 'N00044245', 'cycle': '2020', 'origin': 'Center for Responsive Politics', 'source': 'https://www.opensecrets.org/members-of-congress/contributors?cid=N00044245&cycle=2020', 'notice': "The organizations themselves did not donate, rather the money came from the organization's PAC, its individual members or employees or owners, and those individuals' immediate families."})
