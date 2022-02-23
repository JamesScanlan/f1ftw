from calculate_best_qualifying import calculate_best_qualifying
import get_grand_prix_names
import load_config
import datetime
import calculate_best_qualifying
import get_predictors

def generate_summary(active_year):
    grand_prix_names = get_grand_prix_names.get_grand_prix_names(datetime.date.today(), active_year)

    predictors = get_predictors.get_predictors_as_dictionary(active_year)
    summary = {}
    for predictor in predictors:
        summary[predictors[predictor].full_name()] = {'drivers': {}, 'predictor': predictor}

    for grand_prix_name in grand_prix_names:
        results = calculate_best_qualifying.generate_results(grand_prix_name, active_year)
        for predictor in predictors:        
            for result in results:                
                if result.predictor != None:
                    if result.predictor.full_name() == predictor:
                        if result.driver not in summary[predictor]['drivers']:
                            summary[predictor]['drivers'][result.driver] = {'count': 1, 'scores': [result.points]}
                        else:
                            summary[predictor]['drivers'][result.driver]['count'] += 1
                            summary[predictor]['drivers'][result.driver]['scores'].append(result.points)
    return summary

def analyse_scores(scores):
    total = 0
    for score in scores:
        total += score
    return total, round(total / len(scores),2)

def summarise_progressions(active_year):
    summary = generate_summary(active_year)

    for s in summary:
        monkey = summary[s]['drivers']
        index = 0
        indexes = {}
        for m in monkey:
            indexes[index] = monkey[m]['count']
            index += 1
        
        sorted_indexes = {key: value for key, value in sorted(indexes.items(), key=lambda item: item[1], reverse = True)}
        
        new_drivers = {}
        for i in sorted_indexes:
            new_drivers[list(monkey)[i]] = monkey[list(monkey)[i]]
        
        summary[s]['drivers'] = new_drivers

    for s in summary:
        print(s)
        sub_count = 0
        for driver in summary[s]['drivers']:
            sub_count += summary[s]['drivers'][driver]['count']
            total, average = analyse_scores(summary[s]['drivers'][driver]['scores'])
            print('\t' + str(driver.person_name) + ' Count:' + str(summary[s]['drivers'][driver]['count']) + ' ' + str(summary[s]['drivers'][driver]['scores']) + ' Total:' + str(total) + ' Average: ' + str(average))
        print(sub_count)
        print('\n')

if __name__== "__main__":
    config = load_config.read_config()
    active_year = config.current_year

    summarise_progressions(active_year)
