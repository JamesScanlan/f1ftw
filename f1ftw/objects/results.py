from objects.drivers import Drivers
from objects.person_name import person_name

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
        self.qualifying_results = qualifying_results
        self.race_results = race_results
        self.fastest_lap = fastest_lap
    def get_driver(self, driver_name):
        name = driver_name.split(" ")
        person_name = person_name(name[0],name[1])
        for result in self.qualifying_results:
            if result.driver.person_name == person_name:
                return result.driver
        return Nothing
    def get_drivers(self):
        drivers = Drivers()
        for result in self.qualifying_results:
            drivers.add_object(result.driver)
        return drivers
    def get_qualifying_result(self, driver):
        for qualifying_result in self.qualifying_results:
            if qualifying_result.driver == driver:
                return qualifying_result
        return Nothing
    def get_race_result(self, driver):
        for race_result in self.race_results:
            if race_result.driver == driver:
                return race_result
        return Nothing
