import objects
from load_predictions import ReadPredictions
import datetime

class PredictionTotals(objects.collection_class.CollectionClass):
    def __init__(self):
        super().__init__()
    def AddOrUpdatePredictionTotal(self, prediction_total):
        self[self.UpsertObject(prediction_total)].count += 1
    def AddPredictionTotal(self, prediction_total):
        prediction_total.count=1
        self.AddObject(prediction_total)

class PredictionTotal(object):
    def __init__(self, grand_prix, predictor, prediction):
        self.grand_prix = grand_prix
        self.predictor = predictor
        self.prediction = prediction
        self.count = 0
    def __eq__(self, other):
        return (self.predictor == other.predictor) and (self.prediction == other.prediction)
    def __str__(self):
        return str(self.grand_prix) + " / " + str(self.predictor) + " / " + str(self.prediction) + " / " + str(self.count)

def CreatePredictionTotals(predictions):
    prediction_totals=PredictionTotals()
    for prediction in predictions:
        predictor = prediction.predictor
        qualifying_prediction = prediction.qualifying_prediction
        prediction_totals.AddOrUpdatePredictionTotal(PredictionTotal(prediction.grand_prix, predictor, qualifying_prediction))
    return prediction_totals

def CalculatePredictionPatterns():
    prediction_totals=CreatePredictionTotals(ReadPredictions())
    prediction_totals=sorted(prediction_totals,key = lambda x: (x.count, x.prediction), reverse = True)
    for prediction_total in prediction_totals:
        print(prediction_total)


if __name__== "__main__":
    CalculatePredictionPatterns()
