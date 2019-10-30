import calculate_scores
import objects
import get_grand_prix_names
import load_config

def calculate_average_points(current_year):
    grand_prix_names = get_grand_prix_names.get_grand_prix_names(active_year = current_year)
    predictor_totals = objects.predictor_totals.PredictorTotals()

    for grand_prix_name in grand_prix_names:
        calculation_scores = calculate_scores.CalculateRaceScore(grand_prix_name, current_year)
        race_totals = objects.predictor_totals.PredictorTotals()
        race_totals = calculate_scores.CalculateTotals(race_totals, calculation_scores, False)

        for race_total in race_totals:
            predictor_totals.AddOrUpdatePredictorTotalPoints(race_total)

    for predictor_total in sorted(predictor_totals, key = lambda x: x.points, reverse = True):
        print(str(predictor_total.predictor) + "\t" + str("%.2f" % round(predictor_total.points / len(grand_prix_names),2)) + " points")


if __name__== "__main__":
    config = load_config.read_config()
    calculate_average_points(config.current_year)
