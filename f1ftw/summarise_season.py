from calculate_best_qualifying import calculate_best_qualifying
import get_grand_prix_names
import load_config
import datetime
import calculate_best_qualifying
import calculate_best_race
import calculate_best_progression
import get_predictors
from process_command_line_arguments import CommandLineArgumentsProcessor
import text_file_writer
import console_output_redirector

def generate_team_summary(active_year, class_to_invoke):
    grand_prix_names = get_grand_prix_names.get_grand_prix_names(datetime.date.today(), active_year)
    predictors = get_predictors.get_predictors_as_dictionary(active_year)
    summary = {}
    for predictor in predictors:
        summary[predictors[predictor].full_name()] = {'teams': {}, 'predictor': predictor}

    for grand_prix_name in grand_prix_names:
        results = class_to_invoke.generate_results(grand_prix_name, active_year)
        
        for predictor in predictors:        
            for result in results:
                
                if result.predictor != None:
                    if result.predictor.full_name() == predictor:
                        if result.team not in summary[predictor]['teams']:
                            summary[predictor]['teams'][result.team] = {'count': 1, 'scores': [result.points]}
                        else:
                            summary[predictor]['teams'][result.team]['count'] += 1
                            summary[predictor]['teams'][result.team]['scores'].append(result.points)
    return summary

def generate_driver_summary(active_year, class_to_invoke):
    grand_prix_names = get_grand_prix_names.get_grand_prix_names(datetime.date.today(), active_year)

    predictors = get_predictors.get_predictors_as_dictionary(active_year)
    summary = {}
    for predictor in predictors:
        summary[predictors[predictor].full_name()] = {'drivers': {}, 'predictor': predictor}

    for grand_prix_name in grand_prix_names:
        # results = calculate_best_qualifying.generate_results(grand_prix_name, active_year)
        results = class_to_invoke.generate_results(grand_prix_name, active_year)
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

def get_team_summary_data(active_year, class_to_invoke):
    summary = generate_team_summary(active_year, class_to_invoke)
    
    for predictor_name in summary:
        teams = summary[predictor_name]['teams']
        index = 0
        indexes = {}
        for team in teams:
            indexes[index] = teams[team]['count']
            index += 1
        
        sorted_indexes = {key: value for key, value in sorted(indexes.items(), key=lambda item: item[1], reverse = True)}
        
        new_teams = {}
        for i in sorted_indexes:
            new_teams[list(teams)[i]] = teams[list(teams)[i]]

        for new_team in new_teams:
            total, average = analyse_scores(new_teams[new_team]['scores'])
            new_teams[new_team]['total'] = total
            new_teams[new_team]['average'] = average

        new_teams = dict(sorted(new_teams.items(), key=lambda team: (team[1]['count'],team[1]['total']), reverse=True))
        summary[predictor_name]['teams'] = new_teams

    return summary

def get_driver_summary_data(active_year, class_to_invoke):
    summary = generate_driver_summary(active_year, class_to_invoke)

    for predictor_name in summary:
        drivers = summary[predictor_name]['drivers']
        index = 0
        indexes = {}
        for driver in drivers:
            indexes[index] = drivers[driver]['count']
            index += 1
        
        sorted_indexes = {key: value for key, value in sorted(indexes.items(), key=lambda item: item[1], reverse = True)}
        
        new_drivers = {}
        for i in sorted_indexes:
            new_drivers[list(drivers)[i]] = drivers[list(drivers)[i]]

        for new_driver in new_drivers:
            total, average = analyse_scores(new_drivers[new_driver]['scores'])
            new_drivers[new_driver]['total'] = total
            new_drivers[new_driver]['average'] = average

        # This is an example of sorting a dict inside a dict
        # test_dict = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
        #      'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
        #      'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}}
  
        # # printing original dictionary
        # print("The original dictionary : " + str(test_dict))
        
        # # Sort Nested keys by Value
        # # Using sorted() + generator expression + lamda
        # res = {key : dict(sorted(val.items(), key = lambda ele: ele[1]))
        #     for key, val in test_dict.items()}
            
        # # printing result 
        # print("The sorted dictionary : " + str(res))


        new_drivers = dict(sorted(new_drivers.items(), key=lambda driver: (driver[1]['count'],driver[1]['total']), reverse=True))
        summary[predictor_name]['drivers'] = new_drivers

    return summary

def summarise_season(active_year):
    meta_data = {
                    'driver categories':
                        [
                            {
                                'driver category':'Qualifying',
                                'method':calculate_best_qualifying
                            },
                            {
                                'driver category':'Race', 
                                'method':calculate_best_race
                            }
                        ],
                    'team categories':
                        [
                            {
                                'team category':'Progression',
                                'method':calculate_best_progression
                            }
                        ]
                }
    # I'll forget I did this: James look at the above meta data.  Method calls are being passed in as arguments.

    summary = {}
    for driver_event in meta_data['driver categories']:
        summary[driver_event['driver category']] = get_driver_summary_data(active_year, driver_event['method'])
 
    for team_event in meta_data['team categories']:
        summary[team_event['team category']] = get_team_summary_data(active_year, team_event['method'])

    for driver_event in meta_data['driver categories']:
        print(driver_event['driver category'] + ' Prediction Analysis\n')
        for predictor_name in summary[driver_event['driver category']]:
            print(predictor_name)
            driver_count = 0
            for driver in summary[driver_event['driver category']][predictor_name]['drivers']:
                print('\t' + str(driver.person_name) + 
                        ' Count:' + str(summary[driver_event['driver category']][predictor_name]['drivers'][driver]['count']) 
                        + ' ' 
                        + str(summary[driver_event['driver category']][predictor_name]['drivers'][driver]['scores']) 
                        + ' Total:' + str(summary[driver_event['driver category']][predictor_name]['drivers'][driver]['total']) 
                        + ' Average: ' + str(summary[driver_event['driver category']][predictor_name]['drivers'][driver]['average']))
                driver_count += 1
            print('\n\t' + str(driver_count) + ' drivers selected across season\n')

    for team_event in meta_data['team categories']:
        print(team_event['team category'] + ' Prediction Analysis\n')
        for predictor_name in summary[team_event['team category']]:
            print(predictor_name)
            team_count = 0
            for team in summary[team_event['team category']][predictor_name]['teams']:
                print('\t' + str(team) + 
                        ' Count:' + str(summary[team_event['team category']][predictor_name]['teams'][team]['count']) 
                        + ' ' 
                        + str(summary[team_event['team category']][predictor_name]['teams'][team]['scores']) 
                        + ' Total:' + str(summary[team_event['team category']][predictor_name]['teams'][team]['total']) 
                        + ' Average: ' + str(summary[team_event['team category']][predictor_name]['teams'][team]['average']))
                team_count += 1
            print('\n\t' + str(team_count) + ' teams selected across season\n')

if __name__== "__main__":
    active_year = CommandLineArgumentsProcessor().get_argument(0)
    output_file_name = CommandLineArgumentsProcessor().get_argument(1)
    if active_year == None:
        config = load_config.read_config()
        active_year = config.current_year
    
    if output_file_name != None:
        file_handler = text_file_writer.open_file(output_file_name)
        original_output = console_output_redirector.set_output_to_file(file_handler)

    summarise_season(active_year)

    if output_file_name != None:
        text_file_writer.close_file(file_handler)
        console_output_redirector.set_output_to_console(original_output)


