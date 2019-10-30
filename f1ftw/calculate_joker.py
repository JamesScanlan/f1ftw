import objects

def calculate_joker_score(race_team, qualifying_results, drivers_championship):
    joker_score = 0
    for qualifying_result in [q for q in qualifying_results if q.driver.team == race_team]:
        driver_championship_index = drivers_championship.GetRanking(qualifying_result.driver)
        joker_score += driver_championship_index * (len(qualifying_results) - qualifying_result.position)
    return joker_score

def calculate_joker_scores(predictions, results, drivers_championship):
    calculated_results=[]
    for prediction in predictions:
        joker_score = CalculateJokerScore(prediction.joker_prediction, results.qualifying_results, drivers_championship)
        result = objects.calculation_score_results.CalculationScoreResult(prediction.predictor, joker_score)
        result.log = "For " + str(prediction.predictor) + " joker score for " + str(prediction.joker_prediction) + " = " + str(joker_score)
        calculated_results.append(result)

    calculated_scores = objects.calculation_score_results.CalculationScoreResults(objects.grand_prix_stages.GrandPrixStages.JOKER)
    calculated_scores.results=calculated_results

    return calculated_scores
