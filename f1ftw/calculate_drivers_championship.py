import objects
import load_race_results
import get_grand_prix_names
import load_grands_prix_meta_data
import datetime
import load_config
import helpers
from get_grand_prix_name import get_grand_prix_name_from_command_line_arguments


def calculate_drivers_championship(grand_prix, active_year):
    grand_prix_names = get_grand_prix_names.get_grand_prix_names(get_date_in_context_of_race_weekend(grand_prix, active_year), active_year)

    championship_drivers = objects.championship_drivers.ChampionshipDrivers()

    index = grand_prix_names.index(grand_prix)
    counter=0
    for grand_prix_name in grand_prix_names:
        if counter < index:
            results = load_race_results.read_race_results(grand_prix_name, active_year)
            for result in results.race_results:
                championship_drivers.add_or_update_driver(result.driver, result.points)
            if results.fastest_lap != None:
                fastest_lap = helpers.parse_person_name(results.fastest_lap)
                for result in results.race_results:
                    if result.driver.person_name == fastest_lap:
                        championship_drivers.add_or_update_driver(result.driver, 1)
        counter += 1

    if len(championship_drivers) == 0:
        results = load_race_results.read_race_results(grand_prix_names[0], active_year)
        for result in results.race_results:
            championship_drivers.add_or_update_driver(result.driver, 0)

    championship_drivers.apply_sort()
    championship_drivers.apply_ranking()

    return championship_drivers

def get_date_in_context_of_race_weekend(grand_prix_name, active_year):
    grand_prix_meta_data = load_grands_prix_meta_data.read_grands_prix_meta_data(active_year).get_by_name(grand_prix_name)

    if datetime.datetime.now().date() == grand_prix_meta_data.end_date:
        return grand_prix_meta_data.end_date + datetime.timedelta(days=1)
    else:
        return grand_prix_meta_data.end_date


if __name__ == '__main__':
    config = load_config.read_config()
    grand_prix_name = get_grand_prix_name_from_command_line_arguments(default="Australian")
    drivers = calculate_drivers_championship(grand_prix_name, config.current_year)
    counter = 1
    for driver in drivers:
        print(str(counter) + "\t" + str(driver))
        counter += 1
