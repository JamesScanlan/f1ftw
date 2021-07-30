import objects
from get_driver import get_driver

def calculate_sprint_race_score(sprint_race_driver, sprint_race_results, drivers_championship):
    for race_result in [r for r in sprint_race_results if r.driver == sprint_race_driver]:
        driver_championship_index = drivers_championship.get_ranking(sprint_race_driver)
        race_position = race_result.position

        race_points = 0
        if race_result.points != None:
            race_points = race_result.points
            
        # print(driver_championship_index)
        # print(sprint_race_results)
        # print(race_position)
        # print(race_points)
        race_score = ((len(sprint_race_results) - (race_position)) + race_points) * driver_championship_index
        return race_score

def calculate_sprint_race_scores(predictions, results, drivers_championship):
    calculated_results=[]
    for prediction in predictions:
        race_score = 0
        result = None

        if prediction.race_prediction != None:
            race_driver = get_driver(prediction.sprint_race_prediction, results.race_results)
            race_score = calculate_sprint_race_score(race_driver, results.sprint_race_results, drivers_championship)
            result = objects.calculation_score_results.CalculationScoreResult(prediction.predictor, race_score)
            result.log = "For " + str(prediction.predictor) + " driver " + str(prediction.sprint_race_prediction) + " achieved a sprint race score of " + str(race_score) + " points"
        else:
            result = objects.calculation_score_results.CalculationScoreResult(prediction.predictor, race_score)
            result.log = "For " + str(prediction.predictor) + " no driver was predicted, resulting in a score of " + str(race_score) + " points"
        calculated_results.append(result)

    calculated_scores = objects.calculation_score_results.CalculationScoreResults(objects.grand_prix_stages.GrandPrixStages.SPRINT)
    calculated_scores.results = calculated_results
    return calculated_scores
