import load_grands_prix_meta_data
import objects
import datetime

def GetGrandPrixNames(date_value = datetime.date.today()):
    grands_prix_meta_data = load_grands_prix_meta_data.ReadGrandsPrixMetaData()
    return grands_prix_meta_data.GetBeforeDate(date_value).GetNames()

if __name__== "__main__":
    grand_prix_names=GetGrandPrixNames(datetime.date(2017,12,31))
    for grand_prix_name in grand_prix_names:
        print(grand_prix_name)
