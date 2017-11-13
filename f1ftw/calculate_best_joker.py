import load_race_results
import load_predictions
import calculate_joker
from calculate_drivers_championship import CalculateDriversChampionship
import objects

def CalculateBestJoker(grand_prix_name):
    results = load_race_results.ReadRaceResults(grand_prix_name)
    predictions = load_predictions.ReadPredictions(grand_prix_name)
    drivers_championship = CalculateDriversChampionship(grand_prix_name)

    calculated_results = objects.calculated_results.CalculatedResults()

    qualifying_teams = [t.driver.team for t in results.qualifying_results]
    qualifying_teams = set(qualifying_teams)

    for qualifying_team in qualifying_teams:
        joker_score = calculate_joker.CalculateJokerScore(qualifying_team, results.qualifying_results, drivers_championship)
        calculated_results.AddObject(objects.calculated_results.CalculatedTeamResult(qualifying_team, joker_score))

    for prediction in predictions:
        prediction_team=prediction.joker_prediction
        for calculated_result in [c for c in calculated_results if c.team == prediction_team]:
            calculated_result.predictor=prediction.predictor

    calculated_results.ApplySort()

    print("\nPoints\tTeam (Predictor)\n")
    for calculated_result in calculated_results:
        print(str(calculated_result))
