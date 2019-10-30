import json
import os
import objects

def read_config():
    config = objects.config.Config()
    jsonData = json.load(open(os.path.join(os.path.abspath(".."), "data", "config.json")))
    config.current_year = int(jsonData["Config"]["Current_Year"])
    config.default_race = jsonData["Config"]["Default_Race"]
    return config

if __name__== "__main__":
    config = read_config()
    print(config)
