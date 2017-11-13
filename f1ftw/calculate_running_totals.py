import calculate_scores
import objects
import get_grand_prix_names

grand_prix_names = get_grand_prix_names.GetGrandPrixNames()
predictor_totals = objects.predictor_totals.PredictorTotals()

for grand_prix_name in grand_prix_names:
    print("\n" + grand_prix_name + " GP")
    calculation_scores = calculate_scores.CalculateRaceScore(grand_prix_name)
    race_totals = objects.predictor_totals.PredictorTotals()
    race_totals = calculate_scores.CalculateTotals(race_totals, calculation_scores, False)
    calculate_scores.DisplayTotals(race_totals)

    for race_total in race_totals:
        predictor_totals.AddOrUpdatePredictorTotalPoints(race_total)

print("\nGrand Total")
for predictor_total in predictor_totals:
    print(str(predictor_total.predictor) + " scored " + str(predictor_total.points) + " points.")
