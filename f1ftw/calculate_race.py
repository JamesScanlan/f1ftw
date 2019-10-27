import objects
from get_driver import GetDriver

def CalculateRaceScore(race_driver, race_results, drivers_championship):
    for race_result in [r for r in race_results if r.driver == race_driver]:
        driver_championship_index = drivers_championship.GetRanking(race_driver)
        race_position = race_result.position
        race_points = race_result.points
        race_score = ((len(race_results) - (race_position)) + race_points) * driver_championship_index
        return race_score

def CalculateRaceScores(predictions, results, drivers_championship):
    calculated_results=[]
    for prediction in predictions:
        race_score = 0
        result = None

        if prediction.race_prediction != None:
            race_driver = GetDriver(prediction.race_prediction, results.race_results)
            race_score = CalculateRaceScore(race_driver, results.race_results, drivers_championship)
            result = objects.calculation_score_results.CalculationScoreResult(prediction.predictor, race_score)
            result.log = "For " + str(prediction.predictor) + " driver " + str(prediction.race_prediction) + " achieved a race score of " + str(race_score) + " points"
        else:
            result = objects.calculation_score_results.CalculationScoreResult(prediction.predictor, race_score)
            result.log = "For " + str(prediction.predictor) + " no driver was predicted, resulting in a score of " + str(race_score) + " points"
        calculated_results.append(result)

    calculated_scores = objects.calculation_score_results.CalculationScoreResults(objects.grand_prix_stages.GrandPrixStages.RACE)
    calculated_scores.results = calculated_results
    return calculated_scores
