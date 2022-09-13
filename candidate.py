

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
        if self.cid and self.name and self.state and self.party and self.chamber:
            return self.cid + ' ' + self.name
        else:
            return "Unknown"

    def __repr__(self) -> str:
        return "Candidate(cid={}, name={}, cycle={}, state={}, party={}, chamber={})".format(
            self.cid, self.name, self.cycle, self.state, self.party, self.chamber)
