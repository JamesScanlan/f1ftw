import objects
from get_driver import GetDriver

def CalculateQualifyingSector(position):
    if position <= 10:
        return 3
    else:
        if position <=15:
            return 2
        else:
            return 1

def CalculateQualifyingScore(qualifying_driver, qualifying_results, drivers_championship):
    for qualifying_result in [r for r in qualifying_results if r.driver == qualifying_driver]:
        driver_championship_index = drivers_championship.GetRanking(qualifying_driver)
        qualifying_position = qualifying_result.position
        qualifying_sector=CalculateQualifyingSector(qualifying_position)
        qualifying_score=(len(qualifying_results) - (qualifying_position) + qualifying_sector) * driver_championship_index
        return qualifying_score

def CalculateQualifyingScores(predictions, results, drivers_championship):
    calculated_results=[]
    for prediction in predictions:
        prediction_driver=GetDriver(prediction.qualifying_prediction, results.qualifying_results)
        qualifying_score = CalculateQualifyingScore(prediction_driver, results.qualifying_results, drivers_championship)
        result = objects.calculation_score_results.CalculationScoreResult(prediction.predictor, qualifying_score)
        result.log = "For " + str(prediction.predictor) + " driver " + str(prediction.qualifying_prediction) + " achieved a qualifying score of " + str(qualifying_score) + " points"
        calculated_results.append(result)
    calculated_scores = objects.calculation_score_results.CalculationScoreResults(objects.grand_prix_stages.GrandPrixStages.QUALIFYING)
    calculated_scores.results = calculated_results
    return calculated_scores
