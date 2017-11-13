import load_race_results
from get_grand_prix_name import GetGrandPrixNameFromCommandLineArguments
import get_grand_prix_names


def DoCalculation(grand_prix_name):
    print(grand_prix_name)
    results = load_race_results.ReadRaceResults(grand_prix_name)
    load_race_results.ValidateRaceResults(results)


if __name__ == "__main__":
    grand_prix_name = GetGrandPrixNameFromCommandLineArguments(default="All")
    if grand_prix_name != "All":
        DoCalculation(grand_prix_name)
    else:
        grand_prix_names = get_grand_prix_names.GetGrandPrixNames()
        for grand_prix_name in grand_prix_names:
            DoCalculation(grand_prix_name)
