from objects.collection_class import CollectionClass

class CalculatedDriverResult(object):
    def __init__(self, driver, points):
        self.driver = driver
        self.points = points
        self.predictor = None
    def __str__(self):
        if self.predictor is None:
            return str(self.points) + "\t" + str(self.driver.person_name)
        else:
            return str(self.points) + "\t" + str(self.driver.person_name) + " (" + str(self.predictor) + ")"

class CalculatedTeamResult(object):
    def __init__(self, team, points):
        self.team = team
        self.points = points
        self.predictor = None
    def __str__(self):
        if self.predictor is None:
            return str(self.points) + "\t" + str(self.team)
        else:
            return str(self.points) + "\t" + str(self.team) + " (" + str(self.predictor) + ")"


class CalculatedResults(CollectionClass):
    def __init__(self):
        CollectionClass.__init__(self)
    def ApplySort(self):
        self.objects.sort(reverse=True, key=lambda x:x.points)
