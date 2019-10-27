class PersonName(object):
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
    def __repr__(self):
        return "{}:\tFirst Name: {} Last Name: {}".format(self.__class__.__name__,self.first_name,self.last_name)
    def __eq__(self, other):
        if other is None:
            return False
        return (self.first_name == other.first_name) and (self.last_name == other.last_name)
    def __lt__(self, other):
        return (self.last_name < other.last_name) and (self.first_name < other.first_name)
    def __gt__(self, other):
        return (self.last_name > other.last_name) and (self.first_name > other.first_name)
    def __hash__(self):
        return hash(self.first_name) + hash(self.last_name)
