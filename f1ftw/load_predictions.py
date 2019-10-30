import json
import os
import objects
from helpers import parse_person_name
import load_config

def read_predictions(grand_prix_name = None, active_year = 2018):
    jsonData = json.load(open(os.path.join(os.path.abspath(".."), "data", "Predictions.json" )))
    predictions = []

    for race_year in jsonData["Grands_Prix"]:
        if race_year["Year"] == str(active_year):
            for race in race_year["Races"]:
                if grand_prix_name is None:
                    predictions.extend(iterate_predictions(race, active_year))
                else:
                    if race["Grand_Prix"] == grand_prix_name:
                        predictions.extend(iterate_predictions(race, active_year))
    return predictions

#a classic case of method name not representing the method, or is it?
def iterate_predictions(grand_prix, active_year):
    predictions = []
    for prediction_source in grand_prix["Predictions"]:
        prediction = parse_prediction(grand_prix["Grand_Prix"], prediction_source, active_year)
        predictions.append(prediction)
    return predictions

def handle_empty_prediction(item):
    if len(item) == 0:
        return None
    else:
        return parse_person_name(item)

def parse_prediction(grand_prix, prediction_source, active_year):
    predictor = parse_person_name(prediction_source["Predictor"])
    qualifying_prediction = parse_person_name(prediction_source["Qualifying"])
    race_prediction = handle_empty_prediction(prediction_source["Race"]) #parse_person_name(prediction_source["Race"])
    progression_prediction = objects.team.Team(prediction_source["Progression"])
    if active_year == 2017:
        joker_prediction = objects.team.Team(prediction_source["Joker"])
    else:
        joker_prediction = None
    prediction = objects.predictions.Prediction(grand_prix, predictor, qualifying_prediction, race_prediction, progression_prediction, joker_prediction)
    return prediction

if __name__== "__main__":
    config = load_config.read_config()
    predictions = read_predictions(active_year = config.current_year)
    for prediction in predictions:
        print(prediction)
