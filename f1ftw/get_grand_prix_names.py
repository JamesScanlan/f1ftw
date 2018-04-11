import load_grands_prix_meta_data
import objects
import datetime
import load_config

def GetGrandPrixNames(date_value = datetime.date.today(), active_year = 2018):
    grands_prix_meta_data = load_grands_prix_meta_data.ReadGrandsPrixMetaData(active_year)
    return grands_prix_meta_data.GetBeforeDate(date_value).GetNames()

if __name__== "__main__":
    config = load_config.ReadConfig()
    grand_prix_names=GetGrandPrixNames(datetime.date(int(config.current_year),12,31), config.current_year)
    for grand_prix_name in grand_prix_names:
        print(grand_prix_name)
