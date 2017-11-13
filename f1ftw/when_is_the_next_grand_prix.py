import load_grands_prix_meta_data
import objects
import datetime


grands_prix_meta_data = load_grands_prix_meta_data.ReadGrandsPrixMetaData()
md = grands_prix_meta_data.GetNextGrandPrixMetaData(datetime.date.today())
if md != None:
    print("\nThe next grand prix is the " + md.name + " GP" + " which takes place between " + md.start_date.strftime("%d %b %Y") + " and " + md.end_date.strftime("%d %b %Y"))
else:
    print("Sorry, I don't know.")
