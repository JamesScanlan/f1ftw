import objects
from get_grand_prix_name import GetGrandPrixNameFromCommandLineArguments
import load_config
import load_predictions
import load_race_results

def ProcessProgressionPerformance(grand_prix_name, active_year):
    results = load_race_results.ReadRaceResults(grand_prix_name, active_year)
    #predictions = load_predictions.ReadPredictions(grand_prix_name, active_year)
    drivers = results.GetDrivers()
    drivers.Sort()
    for driver in drivers:
        qualifying_position = results.GetQualifyingResult(driver).position
        race_position = results.GetRaceResult(driver).position
        outcome = (20-race_position) - (20-qualifying_position)
        print(str(driver) + ", " + str(qualifying_position) + ", " + str(race_position) + ", " + str(outcome))

if __name__== "__main__":
    config = load_config.read_config()
    grand_prix_name = GetGrandPrixNameFromCommandLineArguments(default=config.default_race)
    ProcessProgressionPerformance(grand_prix_name, config.current_year)
