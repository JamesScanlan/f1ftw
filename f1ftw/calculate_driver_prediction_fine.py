import objects
from load_predictions import ReadPredictions
import load_config
import helpers
from objects.grand_prix_stages import GrandPrixStages

def GetDriverPredictionCount(predictor, driver, stage, active_year):
    predictions = ReadPredictions(active_year = active_year)
    prediction_count = 0
    for prediction in [p for p in predictions if p.predictor == predictor]:
        if stage == GrandPrixStages.QUALIFYING:
                if prediction.qualifying_prediction == driver:
                    prediction_count = prediction_count + 1
        elif stage == GrandPrixStages.RACE:
                if prediction.race_prediction == driver:
                    prediction_count = prediction_count + 1
    return prediction_count

if __name__== "__main__":
    config = load_config.ReadConfig()
    index = GetDriverPredictionCount(helpers.ParsePersonName("Andrew Chadwick"), helpers.ParsePersonName("Max Verstappen"), GrandPrixStages.RACE, config.current_year)
    print(str(index))
