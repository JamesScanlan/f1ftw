import objects
import load_predictions

def GetPredictors():
    predictions = load_predictions.ReadPredictions()
    predictors=[]
    for prediction in predictions:
        predictors.append(prediction.predictor)
    predictors=set(predictors)
    return list(predictors)

if __name__ == '__main__':
    predictors = GetPredictors()
    for predictor in predictors:
        print(predictor)
