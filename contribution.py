from importlib.metadata import packages_distributions


class Contribution:
    def __init__(self, cid, cycle, contributions, source='https://www.opensecrets.org'):
        self.cid = cid
        self.cycle = cycle
        self.contributions = contributions
        self.source = source

    def __str__(self) -> str:
        if self.cid:
            return self.cid
        else:
            return "Unknown"

    def __repr__(self) -> str:
        return "Contribution(cid ={}, cycle ={})".format(self.cid, self.cycle,)

    def get_contribution_rows(self):
        rows = []
        for entry in self.contributions:
            row = [self.cid, self.cycle, entry['indivs'],
                   entry['org_name'], entry['pacs'], entry['total']]
            rows.append(row)
        return rows
