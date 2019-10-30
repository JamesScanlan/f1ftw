import objects
from load_predictions import ReadPredictions
import datetime
import load_config
import load_grands_prix_meta_data

class PredictionTotal(object):
    def __init__(self, grand_prix, predictor, prediction):
        self.grand_prix = grand_prix
        self.grand_prix_index = 0
        self.predictor = predictor
        self.prediction = prediction
        self.count = 0
    def __eq__(self, other):
        return (self.predictor == other.predictor) and (self.prediction == other.prediction) #and (self.grand_prix == other.grand_prix)
    def __str__(self):
        return str(self.grand_prix) + " / " + str(self.predictor) + " / " + str(self.prediction) + " / " + str(self.count)

def CreatePredictionTotals(predictions):
    prediction_totals = objects.prediction_totals.PredictionTotals()
    for prediction in predictions:
        #print(prediction)
        predictor = prediction.predictor
        qualifying_prediction = prediction.qualifying_prediction
        #prediction_totals.AddOrUpdatePredictionTotal(PredictionTotal(prediction.grand_prix, predictor, qualifying_prediction))
        prediction_totals.AddPredictionTotal(PredictionTotal(prediction.grand_prix, predictor, qualifying_prediction))
    return prediction_totals

def CalculatePredictionPatterns(active_year):
    prediction_totals = CreatePredictionTotals(ReadPredictions(active_year = active_year))
    prediction_totals = ApplyGrandPrixIndex(prediction_totals, active_year)
    prediction_totals=sorted(prediction_totals,key = lambda x: (x.grand_prix_index, x.predictor), reverse = False)
    for prediction_total in prediction_totals:
        print(prediction_total)

def ApplyGrandPrixIndex(prediction_totals, active_year):
    meta_data = load_grands_prix_meta_data.ReadGrandsPrixMetaData(active_year)
    grand_prix_names = meta_data.GetNames()
    index = 1
    for grand_prix_name in grand_prix_names:
        for prediction_total in prediction_totals:
            if prediction_total.grand_prix == grand_prix_name:
                #print("Setting " + grand_prix_name + " index to " + str(index))
                prediction_total.index = index
        index = index + 1
    return prediction_totals

if __name__== "__main__":
    config = load_config.read_config()
    CalculatePredictionPatterns(config.current_year)
