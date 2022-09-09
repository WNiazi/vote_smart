

class Candidate:
    def __init__(self, cid, name, cycle, state, party, chamber, source='https://www.opensecrets.org/members-of-congress/summary'):
        self.cid = cid
        self.name = name
        self.cycle = cycle
        self.state = state
        self.party = party
        self.chamber = chamber
        self.source = source
        self.contribution = []

    def __str__(self) -> str:
        return self.cid + ' ' + self.name

    def __repr__(self) -> str:
        return self.cid + ' ' + self.name
