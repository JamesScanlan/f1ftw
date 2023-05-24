import json
import load_race_results
import text_padding

def get_sorted_results(results):
    parsed_results = {}
    for race_result in results:
        parsed_results[race_result.position] = str(race_result.driver.person_name)

    keys = list(parsed_results.keys())
    keys.sort()
    parsed_results = {key: parsed_results[key] for key in keys}

    return parsed_results

race_name = 'Monaco'

parsed_data = {}
data = json.load(open('data/GPData.json'))
for years in data['Grands_Prix']:
    results_data = load_race_results.read_race_results(race_name, years['Year'])
    if len(results_data.race_results) > 0:
        parsed_data[years['Year']] = {'qualifying':get_sorted_results(results_data.qualifying_results), 'race':get_sorted_results(results_data.race_results)}

for year in parsed_data:
    print('\n\n' + year)

    print(text_padding.pad_right('',5) + text_padding.pad_right('Qualifying', 20) + text_padding.pad_right('Race', 20) + '\n')
    for result in parsed_data[year]['qualifying']:
        print(text_padding.pad_right(str(result),5) + text_padding.pad_right(parsed_data[year]['qualifying'][result], 20) + text_padding.pad_right(parsed_data[year]['race'][result], 20))
        # print(format_item(result, 5) + format_item(parsed_data[year]['qualifying'][result],20))