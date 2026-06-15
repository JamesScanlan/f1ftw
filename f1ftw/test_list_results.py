import load_race_results
from get_grand_prix_name import get_grand_prix_name_from_command_line_arguments
import get_grand_prix_names
import load_config
from objects import results

def list_all_results(grand_prix_name, active_year):
    print(grand_prix_name)
    results = load_race_results.read_race_results(grand_prix_name, active_year)

    print("Qualifying Results")
    list_driver_results(results.qualifying_results)

    print("\nRace Results")
    list_driver_results(results.race_results)


def list_driver_results(results):
    parsed_results = {}
    for result in results:
        parsed_results[result.driver.person_name] = result.position
    sorted_results = sorted(parsed_results.items(), key=lambda item: item[1])
    for sorted_result in sorted_results:
        print(f"{sorted_result[1]}\t{sorted_result[0]}")

if __name__ == "__main__":
    config = load_config.read_config()

    grand_prix_name = get_grand_prix_name_from_command_line_arguments(default = "All")
    if grand_prix_name != "All":
        list_all_results(grand_prix_name, config.current_year)
    else:
        grand_prix_names = get_grand_prix_names.get_grand_prix_names()
        for grand_prix_name in grand_prix_names:
            list_all_results(grand_prix_name, config.current_year)
