import objects
from load_predictions import ReadPredictions
import load_config

config = load_config.ReadConfig()
predictions = sorted(ReadPredictions(active_year = config.current_year), key = lambda Prediction: Prediction.predictor)

print("\n")
if config.current_year == 2017:
    print("Grand Prix\tPredictor\t\tQualifying\t\tRace\t\t\tProgression\tJoker")
    print("==========\t=========\t\t==========\t\t====\t\t\t===========\t=====\n")
else:
    print("Grand Prix\tPredictor\t\tQualifying\t\tRace\t\t\tProgression")
    print("==========\t=========\t\t==========\t\t====\t\t\t===========\n")

for prediction in predictions:
    print(prediction)

print("\n")
