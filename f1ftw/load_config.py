import json
# import os
import objects

def read_config():
    config = objects.config.Config()
    # json_data = json.load(open(os.path.join(os.path.abspath(".."), "data", "config.json")))
    # json_data = json.load(open('data/config.json'))
    json_data = json.load(open('data/config.json'))
    config.current_year = int(json_data["Config"]["Current_Year"])
    config.default_race = json_data["Config"]["Default_Race"]
    return config

if __name__== "__main__":
    config = read_config()
    print(config)
