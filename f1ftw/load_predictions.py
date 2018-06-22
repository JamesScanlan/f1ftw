import json
import os
import objects
from helpers import ParsePersonName
import load_config

def ReadPredictions(grand_prix_name = None, active_year = 2018):
    jsonData = json.load(open(os.path.join(os.path.abspath(".."), "data", "Predictions.json" )))
    predictions = []

    for race_year in jsonData["Grands_Prix"]:
        if race_year["Year"] == str(active_year):
            for race in race_year["Races"]:
                if grand_prix_name is None:
                    predictions.extend(IteratePredictions(race, active_year))
                else:
                    if race["Grand_Prix"] == grand_prix_name:
                        predictions.extend(IteratePredictions(race, active_year))

    return predictions

#a classic case of method name not representing the method, or is it?
def IteratePredictions(grand_prix, active_year):
    predictions=[]
    for prediction_source in grand_prix["Predictions"]:
        prediction = ParsePrediction(grand_prix["Grand_Prix"], prediction_source, active_year)
        predictions.append(prediction)
    return predictions

def ParsePrediction(grand_prix, prediction_source, active_year):
    predictor = ParsePersonName(prediction_source["Predictor"])
    qualifying_prediction = ParsePersonName(prediction_source["Qualifying"])
    race_prediction = ParsePersonName(prediction_source["Race"])
    progression_prediction = objects.team.Team(prediction_source["Progression"])
    if active_year == 2017:
        joker_prediction = objects.team.Team(prediction_source["Joker"])
    else:
        joker_prediction = None
    prediction = objects.predictions.Prediction(grand_prix, predictor, qualifying_prediction, race_prediction, progression_prediction, joker_prediction)
    return prediction

if __name__== "__main__":
    config = load_config.ReadConfig()
    predictions = ReadPredictions(active_year = config.current_year)
    for prediction in predictions:
        print(prediction)
        
