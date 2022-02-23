import get_grand_prix_names
import load_config
import datetime
import calculate_best_progression
import get_predictors

def generate_summary(active_year):
    grand_prix_names = get_grand_prix_names.get_grand_prix_names(datetime.date.today(), active_year)

    predictors = get_predictors.get_predictors_as_dictionary(active_year)
    summary = {}
    for predictor in predictors:
        summary[predictors[predictor].full_name()] = {'teams': {}, 'predictor': predictor}


    for grand_prix_name in grand_prix_names:
        results = calculate_best_progression.generate_results(grand_prix_name, active_year)
        for predictor in predictors:        
            for result in results:
                if result.predictor != None:
                    if result.predictor.full_name() == predictor:
                        if result.team.name not in summary[predictor]['teams']:
                            summary[predictor]['teams'][result.team.name] = {'count': 1, 'scores': [result.points]}
                        else:
                            summary[predictor]['teams'][result.team.name]['count'] += 1
                            summary[predictor]['teams'][result.team.name]['scores'].append(result.points)
    return summary

def summarise_progression(active_year):
    summary = generate_summary(active_year)

    for s in summary:
        monkey = summary[s]['teams']
        index = 0
        indexes = {}
        for m in monkey:
            indexes[index] = monkey[m]['count']
            index += 1
        sorted_indexes = {key: value for key, value in sorted(indexes.items(), key=lambda item: item[1], reverse = True)}
        
        new_teams = {}
        for i in sorted_indexes:
            new_teams[list(monkey)[i]] = monkey[list(monkey)[i]]
        
        summary[s]['teams'] = new_teams



    for s in summary:
        print(s)
        print(summary[s]['teams'])
        
if __name__== "__main__":
    config = load_config.read_config()
    active_year = config.current_year

    summarise_progression(active_year)
