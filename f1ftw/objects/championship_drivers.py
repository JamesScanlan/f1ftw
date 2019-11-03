from objects.collection_class import CollectionClass

class ChampionshipDrivers(CollectionClass):
    def __init__(self):
        CollectionClass.__init__(self)
    def get_index(self, driver):
        index=0
        for championship_driver in self.objects:
            if championship_driver.driver == driver:
                return index
            else:
                index += 1
        return -1
    def add_or_update_driver(self, driver, points):
        index = self.get_index(driver)
        if index > -1:
            self[index].points += points
        else:
            self.add_object(ChampionshipDriver(driver, points))
    def apply_sort(self):
        self.objects.sort(reverse=True, key=lambda x:x.points)
    def apply_ranking(self):
        isFirst=True
        ranking = -1
        rankingPoints = -1
        for championship_driver in self.objects:
            if isFirst:
                rankingPoints = championship_driver.points
                ranking = 1
                isFirst = False
            else:
                if rankingPoints != championship_driver.points:
                    ranking += 1
                    rankingPoints = championship_driver.points
            championship_driver.ranking=ranking
    def get_ranking(self, driver):
        for championship_driver in self.objects:
            if championship_driver.driver == driver:
                return championship_driver.ranking
        return -1


class ChampionshipDriver(object):
    def __init__(self, driver, points):
        self.driver = driver
        self.points = points
        self.ranking = 1
    def __str__(self):
        return str(self.points) + "\t" + str(self.driver)
    def __lt__(self, other):
        return self.points < other.points
    def __eq__(self, other):
        return self.points == other.points
    def __gt__(self, other):
        return self.points > other.points
