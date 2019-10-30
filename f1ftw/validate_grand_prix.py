import objects
import datetime
import load_race_results
from load_grands_prix_meta_data import read_grands_prix_meta_data

def is_grand_prix_known(grand_prix_name, active_year):
    return read_grands_prix_meta_data(active_year).get_by_name(grand_prix_name) != None

def do_results_exist_for_grand_prix(grand_prix_name, active_year):
    return load_race_results.do_results_exist_for_grand_prix(grand_prix_name, active_year)
