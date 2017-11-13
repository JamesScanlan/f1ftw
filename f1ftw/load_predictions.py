import json
import os
import objects
from helpers import ParsePersonName


def ReadPredictions(grand_prix_name=None):
    jsonData = json.load(open(os.path.join(os.path.abspath(".."), "data", "Predictions.json" )))
    predictions = []

    for grand_prix in jsonData["Grands_Prix"]:
        if grand_prix_name is None:
            predictions.extend(IteratePredictions(grand_prix))
        else:
            if grand_prix["Grand_Prix"] == grand_prix_name:
                predictions.extend(IteratePredictions(grand_prix))

    return predictions

#a classic case of method name not representing the method, or is it?
def IteratePredictions(grand_prix):
    predictions=[]
    for prediction_source in grand_prix["Predictions"]:
        prediction = ParsePrediction(grand_prix["Grand_Prix"], prediction_source)
        predictions.append(prediction)
    return predictions

def ParsePrediction(grand_prix, prediction_source):
    predictor = ParsePersonName(prediction_source["Predictor"])
    qualifying_prediction = ParsePersonName(prediction_source["Qualifying"])
    race_prediction = ParsePersonName(prediction_source["Race"])
    progression_prediction = objects.team.Team(prediction_source["Progression"])
    joker_prediction = objects.team.Team(prediction_source["Joker"])
    prediction = objects.predictions.Prediction(grand_prix, predictor, qualifying_prediction, race_prediction, progression_prediction, joker_prediction)
    return prediction
