class RaceResult(object):
    def __init__(self, driver, grid, position):
        self.driver = driver
        self.position = position
        self.grid = grid
        self.points = None

class QualifyingResult(object):
    def __init__(self,driver,position):
        self.driver = driver
        self.position = position

class GrandPrixResults(object):
    def __init__(self,qualifying_results, race_results, fastest_lap = None):
        self.qualifying_results=qualifying_results
        self.race_results=race_results
        self.fastest_lap = fastest_lap
