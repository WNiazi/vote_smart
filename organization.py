
class Organization:
    def __init__(self, organizations):
        self.organizations = organizations

    def __str__(self) -> str:
        if self.organizations:
            return self.organizations
        else:
            return "Unknown"

    def __repr__(self) -> str:
        return "Organization(organizations={})".format(self.organizations)

    def get_organization_row(self):
        row = [self.organizations['cycle'], self.organizations['orgid'], self.organizations['orgname'], self.organizations['total'], self.organizations['indivs'], self.organizations['pacs'], self.organizations['soft'], self.organizations['tot527'], self.organizations['dems'], self.organizations['repubs'],
               self.organizations['lobbying'], self.organizations['outside'], self.organizations['mems_invested'], self.organizations['gave_to_pac'], self.organizations['gave_to_party'], self.organizations['gave_to_cand'], self.organizations['gave_to_527'], self.organizations['source']]
        return row
