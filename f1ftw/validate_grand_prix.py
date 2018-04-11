import objects
import datetime
import load_race_results
from load_grands_prix_meta_data import ReadGrandsPrixMetaData

def IsGrandPrixKnown(grand_prix_name, active_year):
    return ReadGrandsPrixMetaData(active_year).GetByName(grand_prix_name) != None

def DoResultsExistForGrandPrix(grand_prix_name, active_year):
    return load_race_results.DoResultsExistForGrandPrix(grand_prix_name, active_year)
