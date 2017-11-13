import objects
import datetime
import load_race_results
from load_grands_prix_meta_data import ReadGrandsPrixMetaData

def IsGrandPrixKnown(grand_prix_name):
    return ReadGrandsPrixMetaData().GetByName(grand_prix_name) != None

def DoResultsExistForGrandPrix(grand_prix_name):
    return load_race_results.DoResultsExistForGrandPrix(grand_prix_name)
