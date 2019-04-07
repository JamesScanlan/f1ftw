import calculate_scores
import objects
import get_grand_prix_names
import load_config

config = load_config.ReadConfig()

grand_prix_names = get_grand_prix_names.GetGrandPrixNames(active_year = config.current_year)
predictor_totals = objects.predictor_totals.PredictorTotals()

for grand_prix_name in grand_prix_names:
    print("\n" + grand_prix_name + " GP")
    calculation_scores = calculate_scores.CalculateRaceScore(grand_prix_name, config.current_year)
    race_totals = objects.predictor_totals.PredictorTotals()
    race_totals = calculate_scores.CalculateTotals(race_totals, calculation_scores, False)
    calculate_scores.DisplayTotals(race_totals)

    for race_total in race_totals:
        predictor_totals.AddOrUpdatePredictorTotalPoints(race_total)


print("\nGrand Total")
for predictor_total in sorted(predictor_totals, key = lambda x: x.points, reverse = True):
    print(str(predictor_total.predictor) + "\t" + str(predictor_total.points) + " points")
