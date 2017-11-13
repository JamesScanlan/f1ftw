import objects

def CalculateProgressionScore(race_team, race_results, drivers_championship):
    progression_score = 0
    for race_result in [r for r in race_results if r.driver.team == race_team]:
        driver_championship_index = drivers_championship.GetRanking(race_result.driver)
        start_position=race_result.grid
        end_position=race_result.position
        progression_score += (start_position - end_position) * driver_championship_index
    return progression_score

def CalculateProgressionScores(predictions, results, drivers_championship):
    calculated_results=[]
    for prediction in predictions:
        progression_score = CalculateProgressionScore(prediction.progression_prediction, results.race_results, drivers_championship)
        result = objects.calculation_score_results.CalculationScoreResult(prediction.predictor, progression_score)
        result.log = "For " + str(prediction.predictor) + " team progression score for " + str(prediction.progression_prediction) + " = " + str(progression_score) + " points"
        calculated_results.append(result)

    calculated_scores = objects.calculation_score_results.CalculationScoreResults(objects.grand_prix_stages.GrandPrixStages.PROGRESSION)
    calculated_scores.results = calculated_results

    return calculated_scores
