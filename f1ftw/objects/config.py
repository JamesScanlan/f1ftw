class Config(object):
    def __init__(self):
        self.current_year = 0
        self.default_race = ''
    def __str__(self):
        return "Current Year:\t" + str(self.current_year)
    def __repr__(self):
        return "{}:\n\t{}\n\t{}".format(self.__class__.__name__,self.current_year)
