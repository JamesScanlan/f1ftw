import json
import os
import objects
import datetime
import load_config

def ReadGrandsPrixMetaData(active_year):
    grands_prix_meta_data = objects.grands_prix_meta_data.GrandsPrixMetaData()
    jsonData = json.load(open(os.path.join(os.path.abspath(".."), "data", "GrandsPrixMetaData.json")))
    for grand_prix in jsonData["GrandsPrix"]:
        if grand_prix["Year"] == str(active_year):
            for race in grand_prix["Races"]:
                grands_prix_meta_data.AddObject(objects.grands_prix_meta_data.GrandPrixMetaData(race["Name"], datetime.datetime.strptime(race["StartDate"],"%Y-%m-%d").date(), datetime.datetime.strptime(race["EndDate"],"%Y-%m-%d").date()))
    return grands_prix_meta_data

if __name__== "__main__":
    config = load_config.ReadConfig()
    gpmd = ReadGrandsPrixMetaData(config.current_year)
    grand_prix_names = gpmd.GetBeforeDate(datetime.date(2018,12,31)).GetNames()
    for grand_prix_name in grand_prix_names:
        print(grand_prix_name)
