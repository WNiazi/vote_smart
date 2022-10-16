
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

    def get_organization_rows(self):
        rows = []
        for entry in self.organizations:
            row = [entry['cycle'], entry['orgid'], entry['orgname'], entry['total'], entry['individual'], entry['pacs'], entry['soft'], entry['total527'], entry['dems'],
                   entry['repubs'], entry['lobbying'], entry['outside'], entry['mems_invested'], entry['gave_to_pac'], entry['gave_to_party'], entry['gave_to_cand'], entry['source']]
            rows.append(row)
        return rows
