import objects
import load_race_results
import get_grand_prix_names
import load_grands_prix_meta_data
import datetime
import load_config
from get_grand_prix_name import GetGrandPrixNameFromCommandLineArguments


def CalculateDriversChampionship(grand_prix, active_year):
    grand_prix_names = get_grand_prix_names.GetGrandPrixNames(GetDateInContextOfRaceWeekend(grand_prix, active_year), active_year)

    championship_drivers = objects.championship_drivers.ChampionshipDrivers()

    index = grand_prix_names.index(grand_prix)
    counter=0
    for grand_prix_name in grand_prix_names:
        if counter < index:
            results = load_race_results.ReadRaceResults(grand_prix_name, active_year)
            for result in results.race_results:
                championship_drivers.AddOrUpdateDriver(result.driver, result.points)
        counter += 1

    if len(championship_drivers) == 0:
        results=load_race_results.ReadRaceResults(grand_prix_names[0], active_year)
        for result in results.race_results:
            championship_drivers.AddOrUpdateDriver(result.driver, 0)

    championship_drivers.ApplySort()
    championship_drivers.ApplyRanking()

    return championship_drivers

def GetDateInContextOfRaceWeekend(grand_prix_name, active_year):
    grand_prix_meta_data = load_grands_prix_meta_data.ReadGrandsPrixMetaData(active_year).GetByName(grand_prix_name)

    if datetime.datetime.now().date() == grand_prix_meta_data.end_date:
        return grand_prix_meta_data.end_date + datetime.timedelta(days=1)
    else:
        return grand_prix_meta_data.end_date

    #changed from datetime.datetime.now().date() so can generate up to date views of championship


if __name__ == '__main__':
    config = load_config.ReadConfig()
    grand_prix_name = GetGrandPrixNameFromCommandLineArguments(default="Australian")
    drivers = CalculateDriversChampionship(grand_prix_name, config.current_year)
    counter = 1
    for driver in drivers:
        print(str(counter) + "\t" + str(driver))
        counter += 1
