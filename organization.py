
class Organization:
    def __init__(self, cycle, orgid, orgname, total, individual, pacs, soft, total527, dems, repubs, lobbying, outside, mems_invested, gave_to_pac, gave_to_party, gave_to_527, gave_to_cand, source):
        self.cycle = cycle
        self.orgid = orgid
        self.orgname = orgname
        self.total = total
        self.pacs = pacs
        self.individual = individual
        self.soft = soft
        self.total527 = total527
        self.dems = dems
        self.repubs = repubs
        self.lobbying = lobbying
        self.outside = outside
        self. mems_invested = mems_invested
        self.gave_to_pac = gave_to_pac
        self.gave_to_party = gave_to_party
        self.gave_to_527 = gave_to_527
        self.gave_to_cand = gave_to_cand
        self.source = source

    def __str__(self) -> str:
        if self.cid and self.org_name:
            return self.org_name
        else:
            return "Unknown"

    def __repr__(self) -> str:
        return "Organization(org_name={}, total ={}, pac ={}, individual ={})".format(self.cid, self.org_name, self.total, self.pacs, self.individual)

    def get_organization_rows(self):
        rows = []
        for entry in self:
            row = [self.cycle, self.orgid, self.orgname, self.total, self.individual, self.pacs, self.soft, self.total527, self.dems,
                   self.repubs, self.lobbying, self.outside, self.mems_invested, self.gave_to_pac, self.gave_to_party, self.gave_to_cand, self.source]
            rows.append(row)
        return rows
