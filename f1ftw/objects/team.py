class Team(object):
    def __init__(self, name):
        self.name=name
    def __eq__(self, other):
        return self.name == other.name
    def __lt__(self, other):
        return self.name < other.name
    def __gt__(self, other):
        return self.name > other.name    
    def __str__(self):
        return self.name
    def __repr__(self):
        return "{}:\tTeam: {}".format(self.__class__.__name__, self.name)
    def __hash__(self):
        return hash(self.name)
