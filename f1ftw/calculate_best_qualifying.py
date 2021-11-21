import load_race_results
import load_predictions
import calculate_qualifying
from calculate_drivers_championship import calculate_drivers_championship
from get_driver import get_driver
import objects


def generate_results(grand_prix_name, active_year):
    results = load_race_results.read_race_results(grand_prix_name, active_year)
    predictions = load_predictions.read_predictions(grand_prix_name, active_year)
    drivers_championship = calculate_drivers_championship(grand_prix_name, active_year)

    calculated_results = objects.calculated_results.CalculatedResults()

    for result in results.qualifying_results:
        qualifying_driver = result.driver
        qualifying_score = calculate_qualifying.calculate_qualifying_score(qualifying_driver, results.qualifying_results, drivers_championship)
        calculated_results.add_object(objects.calculated_results.CalculatedDriverResult(qualifying_driver, qualifying_score))

    for prediction in predictions:
        prediction_driver = get_driver(prediction.qualifying_prediction, results.qualifying_results)
        for calculated_result in [c for c in calculated_results if c.driver == prediction_driver]:
            calculated_result.predictor = prediction.predictor

    calculated_results.apply_sort()

    # print("\nPoints\tDriver (Predictor)\n")
    # for calculated_result in calculated_results:
    #     print(str(calculated_result))

    return calculated_results


def calculate_best_qualifying(grand_prix_name, active_year):

    results = generate_results(grand_prix_name, active_year)

    print("\nPoints\tTeam (Predictor)\n")
    for calculated_result in results:
        print(str(calculated_result))

if __name__== "__main__":
    calculate_best_qualifying('Qatar',2021)