
class Organization:
    def __init__(self, org_name, total, individual, pacs,  source='https://www.opensecrets.org'):
        self.org_name = org_name
        self.total = total
        self.pacs = pacs
        self.individual = individual
        self.source = source

    def __str__(self) -> str:
        if self.cid and self.org_name:
            return self.org_name
        else:
            return "Unknown"

    def __repr__(self) -> str:
        return "Organization(org_name={}, total ={}, pac ={}, individual ={})".format(self.cid, self.org_name, self.total, self.pacs, self.individual)
