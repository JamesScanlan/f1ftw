import load_race_results
import objects.results
import get_grand_prix_names

for grand_prix_name in get_grand_prix_names.GetGrandPrixNames():
        print("\n" + grand_prix_name)
        results = load_race_results.ReadRaceResults(grand_prix_name)
        load_race_results.ValidateRaceResults(results)
