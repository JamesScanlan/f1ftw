import json
import os
from objects.driver import Driver
import objects
import objects.results
from helpers import ParsePersonName


def CalcRacePoints(position):
    points = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}
    if position > 10:
        return 0
    else:
        return points[position]


def LoadRaceResultsIntoJSON():
    return json.load(open(os.path.join(os.path.abspath(".."), "data", "GPData.json")))


def ReadRaceResults(grand_prix_name):
    jsonData=LoadRaceResultsIntoJSON()

    qualifying_results=[]
    race_results=[]

    for grand_prix_source in jsonData["Grands_Prix"]:
        if grand_prix_source["Grand_Prix"] == grand_prix_name:
                for results_source in grand_prix_source["Results"]:
                    current_driver = Driver(ParsePersonName(results_source["name"]),objects.team.Team(results_source["team"]))

                    qualifying_result = objects.results.QualifyingResult(current_driver, int(results_source["qualifying"]))
                    qualifying_results.append(qualifying_result)

                    race_result = objects.results.RaceResult(current_driver, int(results_source["grid"]), int(results_source["position"]))
                    race_result.points = CalcRacePoints(int(results_source["position"]))
                    race_results.append(race_result)

    return objects.results.GrandPrixResults(qualifying_results, race_results)

def DoResultsExistForGrandPrix(grand_prix_name):
    jsonData=LoadRaceResultsIntoJSON()
    found_results = False
    for grand_prix_source in jsonData["Grands_Prix"]:
        if grand_prix_source["Grand_Prix"] == grand_prix_name:
            found_results = True
    return found_results

def ValidateRaceResults(results):
    qualifying_total=0
    for qualifying_result in results.qualifying_results:
        qualifying_total += qualifying_result.position

    race_total=0
    for race_result in results.race_results:
        race_total += race_result.position

    grid_total = 0
    for grid_result in results.race_results:
        grid_total += grid_result.grid

    print("Qualifying: " + str(qualifying_total))
    print("Grid:" + str(grid_total))
    print("Race: " + str(race_total))