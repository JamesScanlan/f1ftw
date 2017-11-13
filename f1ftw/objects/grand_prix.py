class GrandPrix(object):
    def __init__(self,name):
        self.name=name
        self.teams=None
        self.drivers=None
    def __repr__(self):
        return "{}:\t{}".format(self.__class__.__name__,self.name)
