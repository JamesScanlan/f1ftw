import json
import os
from objects.driver import Driver
import objects
import objects.results
from helpers import parse_person_name
from load_grands_prix_meta_data import read_meta_data_value

def does_race_feature_a_sprint(grand_prix_name, active_year):
    if read_meta_data_value(grand_prix_name, active_year, "Format") == "Sprint":
        return True
    else:
        return False

def was_race_impacted_by_weather(grand_prix_name, active_year):
    if read_meta_data_value(grand_prix_name, active_year, "Outcome") == "RaceImpactedByWeather":
        return True
    else:
        return False

def calc_race_points(position):
    points = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}
    if position > 10:
        return 0
    else:
        return points[position]

def load_race_results_into_json():
    # return json.load(open(os.path.join(os.path.abspath(".."), "data", "GPData.json")))
    return json.load(open('data/GPData.json'))

def read_race_results(grand_prix_name, active_year):
    jsonData = load_race_results_into_json()

    qualifying_results = []
    sprint_race_results = []
    race_results = []
    fastest_lap = ""

    for race_year in jsonData["Grands_Prix"]:
        if race_year["Year"] == str(active_year):
            for race in race_year["Races"]:
                if race["Grand_Prix"] == grand_prix_name:
                    was_race_weather_affected = was_race_impacted_by_weather(grand_prix_name, active_year)

                    for results_source in race["Results"]:
                        current_driver = Driver(parse_person_name(results_source["name"]),objects.team.Team(results_source["team"]))
                        
                        qualifying_result = objects.results.QualifyingResult(current_driver, int(results_source["qualifying"]))
                        qualifying_results.append(qualifying_result)
                        
                        if does_race_feature_a_sprint(race["Grand_Prix"], active_year):
                            sprint_race_result = objects.results.SprintRaceResult(current_driver, int(results_source["qualifying"]), int(results_source["sprint"])) #(current_driver, int(results_source["sprint"]))
                        else:
                            sprint_race_result = None
                        sprint_race_results.append(sprint_race_result)

                        race_result = objects.results.RaceResult(current_driver, int(results_source["grid"]), int(results_source["position"]))
                        race_result.points = calc_race_points(int(results_source["position"]))
                        if was_race_weather_affected ==True:
                            race_result.points = race_result.points / 2
                        race_results.append(race_result)
                    if "fastest_lap" in race:
                        fastest_lap = race["fastest_lap"]
                    else:
                        fastest_lap = None

    return objects.results.GrandPrixResults(qualifying_results, sprint_race_results, race_results, fastest_lap)

def do_results_exist_for_grand_prix(grand_prix_name, active_year):
    jsonData = load_race_results_into_json()
    found_results = False
    for race_year in jsonData["Grands_Prix"]:
        if race_year["Year"] == str(active_year):
            for race in race_year["Races"]:
                if race["Grand_Prix"] == grand_prix_name:
                    found_results = True
    return found_results

def validate_race_results(results):
    qualifying_total = 0
    for qualifying_result in results.qualifying_results:
        qualifying_total += qualifying_result.position

    race_total = 0
    for race_result in results.race_results:
        race_total += race_result.position

    grid_total = 0
    for grid_result in results.race_results:
        grid_total += grid_result.grid

    print("Qualifying: " + str(qualifying_total))
    print("Grid:" + str(grid_total))
    print("Race: " + str(race_total))
