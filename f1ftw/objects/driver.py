class Driver(object):
    def __init__(self,person_name,team):
        self.person_name=person_name
        self.team=team
    def __str__(self):
        return str(self.person_name) + " " + str(self.team)
    def __repr__(self):
        return "{}:\n\t{}\n\t{}".format(self.__class__.__name__,self.person_name,self.team)
    def __eq__(self,other):
        return (self.person_name == other.person_name) and (self.team == other.team)
