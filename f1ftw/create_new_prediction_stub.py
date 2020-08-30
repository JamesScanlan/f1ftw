import load_config
import json
import os
import objects

def clean_predictions(grand_prix):
    new_grand_prix = grand_prix.copy()
    new_grand_prix['Grand_Prix'] = ''
    for prediction in new_grand_prix['Predictions']:
        prediction['Qualifying'] = ''
        prediction['Race'] = ''
        prediction['Progression'] = ''
    return new_grand_prix

def write_data(file_name, contents):
    with open(file_name, 'w') as fp:
        json.dump(contents, fp, indent=4)

def create_empty_predictions(current_year):
    jsonData = json.load(open(os.path.join(os.path.abspath(".."), "data", "Predictions.json")))

    for grand_prix in jsonData['Grands_Prix']:
        if grand_prix['Year'] == str(current_year):
            grand_prix['Races'].append(clean_predictions(grand_prix['Races'][len(grand_prix['Races']) -1 ]))

    write_data(os.path.join(os.path.abspath('..'), 'data', 'Predictions2.json'), jsonData.copy())

if __name__== "__main__":

    config = load_config.read_config()
    create_empty_predictions(config.current_year)

    print('Empty set of predictions created')
