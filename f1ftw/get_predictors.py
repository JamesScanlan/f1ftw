import objects
import load_predictions
import load_config

def get_predictors(active_year):
    predictions = load_predictions.read_predictions(None, active_year)
    predictors = []
    for prediction in predictions:
        predictors.append(prediction.predictor)
    predictors = set(predictors)
    return list(predictors)

def get_predictors_as_dictionary(active_year):
    predictors = get_predictors(active_year)
    predictors_dict = {}
    for predictor in predictors:
        predictors_dict[predictor.full_name()] = predictor
    # print(predictors)
    return predictors_dict

if __name__ == '__main__':
    config = load_config.read_config()
    predictors = get_predictors(config.current_year)
    for predictor in predictors:
        print(predictor)
