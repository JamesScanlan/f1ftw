import objects
import calculate_scores
from get_grand_prix_name import GetGrandPrixNameFromCommandLineArguments
import validate_grand_prix
import validate_predictions
from conditions.condition import Condition
import load_config


def process_race_scores(grand_prix_name, active_year):
    predictor_totals = objects.predictor_totals.PredictorTotals()
    calculation_scores = calculate_scores.CalculateRaceScore(grand_prix_name, active_year)
    predictor_totals = calculate_scores.CalculateTotals(predictor_totals, calculation_scores)
    print("\nRace Total:")
    calculate_scores.DisplayTotals(predictor_totals)

def validate_conditions(grand_prix_name, active_year):
    check_conditions=[]
    check_conditions.append(Condition(validate_grand_prix.IsGrandPrixKnown(grand_prix_name, active_year), "\nSorry, I don't recognise the " + grand_prix_name + " GP as being valid."))
    check_conditions.append(Condition(validate_grand_prix.DoResultsExistForGrandPrix(grand_prix_name, active_year), "\nSorry, the " + grand_prix_name + " GP has not taken place yet."))
    check_conditions.append(Condition(validate_predictions.DoPredictionsExistForGrandPrix(grand_prix_name, active_year),"\nSorry, no predictions for " + grand_prix_name + " are known."))
    all_conditions_passed = False
    for check_condition in check_conditions:
        if check_condition.Evaluate() == True:
            all_conditions_passed = True
        else:
            #else:grand_prix_source
            all_conditions_passed = False
            print(check_condition.message)
            break
    return all_conditions_passed

if __name__== "__main__":
    config = load_config.ReadConfig()
    grand_prix_name = GetGrandPrixNameFromCommandLineArguments(default=config.default_race)

    if validate_conditions(grand_prix_name, config.current_year):
        process_race_scores(grand_prix_name, config.current_year)
