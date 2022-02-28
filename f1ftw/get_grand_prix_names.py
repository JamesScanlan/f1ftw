import load_grands_prix_meta_data
# import objects
import datetime
import load_config

def get_all_grand_prix_for_season(active_year = 2019):
    return load_grands_prix_meta_data.read_grands_prix_meta_data(active_year).get_names()

def get_grand_prix_names(date_value = datetime.date.today(), active_year = 2018):
    grands_prix_meta_data = load_grands_prix_meta_data.read_grands_prix_meta_data(active_year)
    return grands_prix_meta_data.get_before_previous_or_current_race_weekends(date_value).get_names()

if __name__== "__main__":
    config = load_config.read_config()
    grand_prix_names = get_grand_prix_names(datetime.date(int(config.current_year),12,31), config.current_year)
    for grand_prix_name in grand_prix_names:
        print(grand_prix_name)
