import load_grands_prix_meta_data
import objects
import datetime
import load_config

config = load_config.ReadConfig()

grands_prix_meta_data = load_grands_prix_meta_data.ReadGrandsPrixMetaData(config.current_year)
md = grands_prix_meta_data.GetNextGrandPrixMetaData(datetime.date.today())
if md != None:
    print("\nThe next grand prix is the " + md.name + " GP" + " which takes place between " + md.start_date.strftime("%d %b %Y") + " and " + md.end_date.strftime("%d %b %Y") + "\n")
else:
    print("Sorry, I don't know.")
