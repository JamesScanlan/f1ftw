import load_race_results
import load_predictions
import calculate_progression
from calculate_drivers_championship import calculate_drivers_championship
import objects

def calculate_best_progression(grand_prix_name, active_year):
    results = load_race_results.read_race_results(grand_prix_name, active_year)
    predictions = load_predictions.read_predictions(grand_prix_name, active_year)
    drivers_championship = calculate_drivers_championship(grand_prix_name, active_year)

    calculated_results = objects.calculated_results.CalculatedResults()

    race_teams = [t.driver.team for t in results.race_results]
    race_teams = set(race_teams)

    for race_team in race_teams:
        progression_score = calculate_progression.calculate_progression_score(race_team, results.race_results, drivers_championship)
        calculated_results.AddObject(objects.calculated_results.CalculatedTeamResult(race_team, progression_score))

    for prediction in predictions:
        prediction_team = prediction.progression_prediction
        for calculated_result in [c for c in calculated_results if c.team == prediction_team]:
            calculated_result.predictor=prediction.predictor

    calculated_results.ApplySort()

    print("\nPoints\tTeam (Predictor)\n")
    for calculated_result in calculated_results:
        print(str(calculated_result))
