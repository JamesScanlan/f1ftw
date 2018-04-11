import objects
import datetime
import load_race_results
from load_predictions import ReadPredictions

def DoPredictionsExistForGrandPrix(grand_prix_name, active_year):
    return len(ReadPredictions(grand_prix_name, active_year)) > 0
