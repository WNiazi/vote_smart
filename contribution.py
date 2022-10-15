from importlib.metadata import packages_distributions


class Contribution:
    def __init__(self, cid, cycle, name, contributions, source='https://www.opensecrets.org'):
        self.cid = cid
        self.cycle = cycle
        self.name = name
        self.contributions = contributions
        self.source = source

    def __str__(self) -> str:
        if self.cid:
            return self.cid
        else:
            return "Unknown"

    def __repr__(self) -> str:
        return "Contribution(cid ={}, cycle ={}, org_name = {}, information={})".format(self.cid, self.cycle, self.org_name, self.information)

    def get_contribution_rows(self):
        rows = []
        for entry in self.contributions:
            row = [self.cid, self.cycle, self.name, entry['indivs'],
                   entry['org_name'], entry['pacs'], entry['total']]
            rows.append(row)
        return rows
