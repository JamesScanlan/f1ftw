import calculate_scores
import objects
import get_grand_prix_names
import load_config

def calculate_running_totals(current_year, display_breakdown = True):
    grand_prix_names = get_grand_prix_names.get_grand_prix_names(active_year = current_year)
    predictor_totals = objects.predictor_totals.PredictorTotals()

    for grand_prix_name in grand_prix_names:
        if display_breakdown == True:
            print("\n" + grand_prix_name + " GP")
        calculation_scores = calculate_scores.calculate_race_score(grand_prix_name, current_year)
        race_totals = objects.predictor_totals.PredictorTotals()
        race_totals = calculate_scores.calculate_totals(race_totals, calculation_scores, False)
        if display_breakdown == True:
            calculate_scores.display_totals(race_totals)

        for race_total in race_totals:
            predictor_totals.add_or_update_predictor_total_points(race_total)
    if display_breakdown == True:
        print("\nGrand Total")

    for predictor_total in sorted(predictor_totals, key = lambda x: x.points, reverse = True):
        print(str(predictor_total.predictor) + "\t" + str(predictor_total.points) + " points")

if __name__== "__main__":
    config = load_config.read_config()
    calculate_running_totals(config.current_year)
