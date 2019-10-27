import load_race_results
import load_predictions
import calculate_race
from calculate_drivers_championship import CalculateDriversChampionship
from get_driver import GetDriver
import objects

def CalculateBestRace(grand_prix_name, active_year):
    results = load_race_results.ReadRaceResults(grand_prix_name, active_year)
    predictions = load_predictions.read_predictions(grand_prix_name, active_year)
    drivers_championship = CalculateDriversChampionship(grand_prix_name, active_year)

    calculated_results = objects.calculated_results.CalculatedResults()

    for result in results.race_results:
        race_driver = result.driver
        race_score = calculate_race.CalculateRaceScore(race_driver, results.race_results, drivers_championship)
        calculated_results.AddObject(objects.calculated_results.CalculatedDriverResult(race_driver, race_score))

    for prediction in predictions:
        prediction_driver=GetDriver(prediction.race_prediction, results.race_results)
        for calculated_result in [c for c in calculated_results if c.driver == prediction_driver]:
            calculated_result.predictor=prediction.predictor

    calculated_results.ApplySort()

    print("\nPoints\tDriver (Predictor)\n")
    for calculated_result in calculated_results:
        print(str(calculated_result))
