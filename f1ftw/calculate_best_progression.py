import load_race_results
import load_predictions
import calculate_progression
from calculate_drivers_championship import CalculateDriversChampionship
import objects

def CalculateBestProgression(grand_prix_name):
    results = load_race_results.ReadRaceResults(grand_prix_name)
    predictions = load_predictions.ReadPredictions(grand_prix_name)
    drivers_championship = CalculateDriversChampionship(grand_prix_name)

    calculated_results = objects.calculated_results.CalculatedResults()

    race_teams = [t.driver.team for t in results.race_results]
    race_teams = set(race_teams)

    for race_team in race_teams:
        progression_score = calculate_progression.CalculateProgressionScore(race_team, results.race_results, drivers_championship)
        calculated_results.AddObject(objects.calculated_results.CalculatedTeamResult(race_team, progression_score))

    for prediction in predictions:
        prediction_team=prediction.progression_prediction
        for calculated_result in [c for c in calculated_results if c.team == prediction_team]:
            calculated_result.predictor=prediction.predictor

    calculated_results.ApplySort()

    print("\nPoints\tTeam (Predictor)\n")
    for calculated_result in calculated_results:
        print(str(calculated_result))
