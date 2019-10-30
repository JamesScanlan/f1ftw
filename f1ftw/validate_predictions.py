import objects
import datetime
import load_race_results
from load_predictions import read_predictions

def do_predictions_exist_for_grand_prix(grand_prix_name, active_year):
    return len(read_predictions(grand_prix_name, active_year)) > 0
