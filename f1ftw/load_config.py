import json
import os
import objects

def ReadConfig():
    config = objects.config.Config()
    jsonData = json.load(open(os.path.join(os.path.abspath(".."), "data", "config.json")))
    config.current_year = int(jsonData["Config"]["Current_Year"])
    return config

if __name__== "__main__":
    config = ReadConfig()
    print(config)
