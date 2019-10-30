import objects
from load_predictions import read_predictions
import load_config
import helpers
from objects.grand_prix_stages import GrandPrixStages
from load_grands_prix_meta_data import read_grands_prix_meta_data
import datetime

def get_driver_prediction_count(grand_prix, predictor, driver, stage, active_year):
    predictions = read_predictions(grand_prix_name = grand_prix, active_year = active_year)
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
    config = load_config.read_config()
    gpmd = read_grands_prix_meta_data(config.current_year)
    grand_prix_names = gpmd.get_before_date(datetime.date.today()).get_names()
    for grand_prix_name in grand_prix_names:
        index = get_driver_prediction_count(grand_prix_name, helpers.parse_person_name("Andrew Chadwick"), helpers.parse_person_name("Max Verstappen"), GrandPrixStages.RACE, config.current_year)
        print(grand_prix_name + " " + str(index))
