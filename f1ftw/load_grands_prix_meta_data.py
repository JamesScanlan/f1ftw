import json
import os
import objects
import datetime

def ReadGrandsPrixMetaData():
    grands_prix_meta_data = objects.grands_prix_meta_data.GrandsPrixMetaData()
    jsonData = json.load(open(os.path.join(os.path.abspath(".."), "/data", "GrandsPrixMetaData.json")))
    for grand_prix in jsonData["GrandsPrix"]:
        grands_prix_meta_data.AddObject(objects.grands_prix_meta_data.GrandPrixMetaData(grand_prix["Name"], datetime.datetime.strptime(grand_prix["StartDate"],"%Y-%m-%d").date(), datetime.datetime.strptime(grand_prix["EndDate"],"%Y-%m-%d").date()))
    return grands_prix_meta_data

if __name__== "__main__":
    gpmd=ReadGrandsPrixMetaData()
    grand_prix_names=gpmd.GetBeforeDate(datetime.date(2017,7,10)).GetNames()
    for grand_prix_name in grand_prix_names:
        print(grand_prix_name)
