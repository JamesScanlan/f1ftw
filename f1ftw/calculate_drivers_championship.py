import objects
import load_race_results
import get_grand_prix_names
import load_grands_prix_meta_data
import datetime

def CalculateDriversChampionship(grand_prix):
    grand_prix_names = get_grand_prix_names.GetGrandPrixNames(GetDateInContextOfRaceWeekend(grand_prix))

    championship_drivers = objects.championship_drivers.ChampionshipDrivers()

    index=grand_prix_names.index(grand_prix)
    counter=0
    for grand_prix_name in grand_prix_names:
        if counter < index:
            results = load_race_results.ReadRaceResults(grand_prix_name)
            for result in results.race_results:
                championship_drivers.AddOrUpdateDriver(result.driver, result.points)
        counter += 1

    if len(championship_drivers) == 0:
        results=load_race_results.ReadRaceResults(grand_prix_names[0])
        for result in results.race_results:
            championship_drivers.AddOrUpdateDriver(result.driver, 0)

    championship_drivers.ApplySort()
    championship_drivers.ApplyRanking()

    return championship_drivers

def GetDateInContextOfRaceWeekend(grand_prix_name):
    grand_prix_meta_data = load_grands_prix_meta_data.ReadGrandsPrixMetaData().GetByName(grand_prix_name)

    if datetime.datetime.now().date() == grand_prix_meta_data.end_date:
        return (datetime.datetime.now() + datetime.timedelta(days=1)).date()
    else:
        return datetime.datetime.now().date()
