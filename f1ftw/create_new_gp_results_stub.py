import load_config
import json
import os
import objects
import shutil

def clean_results(grand_prix):
    new_grand_prix = grand_prix.copy()
    new_grand_prix['Grand_Prix'] = ''
    for prediction in new_grand_prix['Results']:
        prediction['grid'] = ''
        prediction['position'] = ''
        prediction['qualifying'] = ''
    return new_grand_prix

def is_integer(value: str, *, base: int=10) -> bool:
    try:
        int(value, base=base)
        return True
    except ValueError:
        return False

def get_digit_part(word):
    index = -1
    for counter in range(len(word)-1,0,-1):
        print(counter,word[counter])
        if is_integer(word[counter]):
            index = counter
        else:
            break
    if index > -1:
        return int(work[index:len(word)])
    else:
        return -1

def create_revision_file_name(file_name):
    position = file_name.find('.')
    file_extension = file_name[position+1:len(file_name)]
    file_name_part = file_name[0:position]
    print(get_digit_part(file_name_part))


def backup_data(file_name):
    shutil.copyfile(source_file, destination_file)

def write_data(file_name, contents):
    with open(file_name, 'w') as fp:
        json.dump(contents, fp, indent=4)

def create_empty_results(current_year, file_name):
    jsonData = json.load(open(os.path.join(os.path.abspath('..'), 'data', file_name)))

    for grand_prix in jsonData['Grands_Prix']:
        if grand_prix['Year'] == str(current_year):
            grand_prix['Races'].append(clean_results(grand_prix['Races'][len(grand_prix['Races']) -1 ]))

    new_file_name = create_revision_file_name(file_name)
    write_data(os.path.join(os.path.abspath('..'), 'data', 'GPData2.json'), jsonData.copy())

if __name__== "__main__":

    config = load_config.read_config()
    create_empty_results(config.current_year, 'GPData.json')

    print('Empty set of results created')
