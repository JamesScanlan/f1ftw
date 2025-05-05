import objects
import load_predictions
import load_race_results
from calculate_qualifying import calculate_qualifying_scores
from calculate_race import calculate_race_scores
from calculate_sprint_race import calculate_sprint_race_scores
from calculate_progression import calculate_progression_scores
from calculate_joker import calculate_joker_scores
from calculate_drivers_championship import calculate_drivers_championship
from load_grands_prix_meta_data import read_meta_data_value

def does_race_feature_a_sprint(grand_prix_name, active_year):
    if read_meta_data_value(grand_prix_name, active_year, "Format") == "Sprint":
        return True
    else:
        return False
    

def get_grand_prix_stage_name(stage):
    stages = ["Qualifying","Race","Progression","Joker","Sprint"]
    return stages[stage.value-1]

def calculate_race_score(grand_prix_name, active_year):
    results = load_race_results.read_race_results(grand_prix_name, active_year)
    predictions = load_predictions.read_predictions(grand_prix_name, active_year)
    drivers_championship = calculate_drivers_championship(grand_prix_name, active_year)
    calculation_scores = []


    if does_race_feature_a_sprint(grand_prix_name, active_year):
        calculation_scores.append(calculate_sprint_race_scores(predictions, results, drivers_championship))
    calculation_scores.append(calculate_qualifying_scores(predictions, results, drivers_championship))
    calculation_scores.append(calculate_race_scores(predictions, results, drivers_championship))
    calculation_scores.append(calculate_progression_scores(predictions, results, drivers_championship))
    if active_year == 2017:
        calculation_scores.append(calculate_joker_scores(predictions, results, drivers_championship))
    return calculation_scores

def calculate_totals(predictor_totals, calculation_scores, print_totals=True):
    for calculation_score in calculation_scores:
        if print_totals:
            print("\n" + get_grand_prix_stage_name(calculation_score.stage) + ":")
        for stage_score in calculation_score.results:
            if print_totals:
                print(stage_score.log)
            predictor_totals.add_or_update_predictor_total_points(objects.predictor_totals.PredictorTotal(stage_score.predictor, stage_score.score))
    return predictor_totals

def display_totals(predictor_totals):
    for predictor_total in predictor_totals:
        if predictor_total.predictor != None:
            print(str(predictor_total.predictor) + " scored " + str(predictor_total.points) + " points.")
