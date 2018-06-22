import objects
import load_predictions
import load_race_results
from calculate_qualifying import CalculateQualifyingScores
from calculate_race import CalculateRaceScores
from calculate_progression import CalculateProgressionScores
from calculate_joker import CalculateJokerScores
from calculate_drivers_championship import CalculateDriversChampionship

def GetGrandPrixStageName(stage):
    stages=["Qualifying","Race","Progression","Joker"]
    return stages[stage.value-1]

def CalculateRaceScore(grand_prix_name, active_year):
    results = load_race_results.ReadRaceResults(grand_prix_name, active_year)
    predictions = load_predictions.ReadPredictions(grand_prix_name, active_year)
    drivers_championship = CalculateDriversChampionship(grand_prix_name, active_year)
    calculation_scores = []

    calculation_scores.append(CalculateQualifyingScores(predictions, results, drivers_championship))
    calculation_scores.append(CalculateRaceScores(predictions, results, drivers_championship))
    calculation_scores.append(CalculateProgressionScores(predictions, results, drivers_championship))
    if active_year == 2017:
        calculation_scores.append(CalculateJokerScores(predictions, results, drivers_championship))
    return calculation_scores

def CalculateTotals(predictor_totals, calculation_scores, print_totals=True):
    for calculation_score in calculation_scores:
        if print_totals:
            print("\n" + GetGrandPrixStageName(calculation_score.stage) + ":")
        for stage_score in calculation_score.results:
            if print_totals:
                print(stage_score.log)
            predictor_totals.AddOrUpdatePredictorTotalPoints(objects.predictor_totals.PredictorTotal(stage_score.predictor, stage_score.score))
    return predictor_totals

def DisplayTotals(predictor_totals):
    for predictor_total in predictor_totals:
        print(str(predictor_total.predictor) + " scored " + str(predictor_total.points) + " points.")
