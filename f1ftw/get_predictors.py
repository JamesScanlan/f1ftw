import objects
import load_predictions
import load_config

def GetPredictors(active_year):
    predictions = load_predictions.read_predictions(None, active_year)
    predictors=[]
    for prediction in predictions:
        predictors.append(prediction.predictor)
    predictors=set(predictors)
    return list(predictors)

if __name__ == '__main__':
    config = load_config.read_config()
    predictors = GetPredictors(config.current_year)
    for predictor in predictors:
        print(predictor)
