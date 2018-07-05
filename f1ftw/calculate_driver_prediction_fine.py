import objects
from load_predictions import ReadPredictions
import load_config
import helpers
from objects.grand_prix_stages import GrandPrixStages
from load_grands_prix_meta_data import ReadGrandsPrixMetaData
from datetime import datetime

def GetDriverPredictionCount(grand_prix, predictor, driver, stage, active_year):
    predictions = ReadPredictions(grand_prix_name = grand_prix, active_year = active_year)
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
    gpmd = ReadGrandsPrixMetaData(config.current_year)
    grand_prix_names = gpmd.GetBeforeDate(datetime.date.today()).GetNames()
    for grand_prix_name in grand_prix_names:
        index = GetDriverPredictionCount(grand_prix_name, helpers.ParsePersonName("Andrew Chadwick"), helpers.ParsePersonName("Max Verstappen"), GrandPrixStages.RACE, config.current_year)
        print(grand_prix_name + " " + str(index))
