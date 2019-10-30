import objects
from process_command_line_arguments import CommandLineArguments
import load_config
import load_predictions
import load_race_results
from get_grand_prix_names import GetGrandPrixNames

def ProcessProgressionPerformanceForDriver(driver_name, active_year):
    grand_prix_names = GetGrandPrixNames(active_year = active_year)
    for grand_prix_name in grand_prix_names:
        results = load_race_results.ReadRaceResults(grand_prix_name, active_year)
        driver = results.GetDriver(driver_name)
        qualifying_position = results.GetQualifyingResult(driver).position
        race_position = results.GetRaceResult(driver).position
        outcome = (20-race_position) - (20-qualifying_position)
        print(str(grand_prix_name) + ", " + str(qualifying_position) + ", " + str(race_position) + ", " + str(outcome))


if __name__== "__main__":
    config = load_config.read_config()
    args = CommandLineArguments()
    driver_name = args[0]

    print("Progression information for driver " + driver_name +"\n")

    ProcessProgressionPerformanceForDriver(driver_name, config.current_year)
