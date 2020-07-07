import get_grand_prix_names
import calculate_race_scores
import load_config
import datetime
from objects.grand_prix_stages import GrandPrixStages
from load_predictions import read_predictions_as_dictionary
from process_command_line_arguments import CommandLineArgumentsProcessor
#from calculate_race_scores import calculate_race_scores
from calculate_scores import calculate_race_score

def evaluate_results(calculation_results):
    outcome_result = None
    first = True
    for calculation_result in calculation_results:
        if first:
            outcome_result = calculation_result
            first = False
        else:
            if calculation_result.score > outcome_result.score:
                outcome_result = calculation_result
    return outcome_result

def get_best_stage(grand_prix_stage, calculation_scores):
    best_result_from_gp_weekend = None
    for calculation_score in calculation_scores:
        if calculation_score.stage == grand_prix_stage:
            best_result_from_gp_weekend = evaluate_results(calculation_score.results)
    return best_result_from_gp_weekend


#this is all bollocks....need to read into a flat structure and sort it:: DICTIONARY O'CLOCK
class OutcomeResult(object):
    def __init__(self):
        self.result = None
        self.count = 0
        self.total = 0
    def average(self):
        return self.total / self.count
    def add_outcome_result(self, result):
        if self.result == None:
            self.result = result
            self.count = 1
            self.total = 0
        else:
            if result.score > self.result.score:
                self.result = result
                self.count += 1
                self.total += result.score
    def __str__(self):
        return "{} Result: {} Count: {} Total: {} Average: {}".format(self.__class__.__name__,self.result, self.count, self.total, self.total / self.count)
    # def __repr__(self):
    #     return "{} Result:{} Count:{} Total:{} Average:{}".format(self.__class__.__name__,self.result, self.count, self.total, self.average)

def read_results_as_dictionary(grand_prix_name, active_year):
    #predictor_totals, calculation_scores, predictor_totals = calculate_race_scores(grand_prix_name, active_year, False)
    #for predictor_total in predictor_totals:
    #    print(predictor_total)
    calculation_score_results = calculate_race_score(grand_prix_name, active_year)
    for calculation_score_result in calculation_score_results:
        print(calculation_score_result.stage)
        for calculation_score in calculation_score_result.results:
            print(calculation_score)
    return {'llama':None}

def summarise_season(active_year):
    season = {}
    grand_prix_names = get_grand_prix_names.get_grand_prix_names(datetime.date.today(), active_year)
    for grand_prix_name in grand_prix_names:
        grand_prix_structure = {}
        grand_prix_structure['predictions'] = read_predictions_as_dictionary(grand_prix_name, active_year)
        grand_prix_structure['results'] = read_results_as_dictionary(grand_prix_name, active_year)
        predictions = {'grand_prix_summary': grand_prix_structure}
        season[grand_prix_name] = predictions
    print(season['Australian']['grand_prix_summary']['results'])


if __name__== "__main__":
    config = load_config.read_config()
    clap = CommandLineArgumentsProcessor()
    active_year = datetime.date.today().year -1
    active_year = clap.get_argument(0)
    if active_year == None:
        print("Please provide a year as a command line argument")
        exit()
    # grand_prix_names = get_grand_prix_names.get_grand_prix_names(datetime.date.today(), active_year)

    # best_qualifying_result = OutcomeResult()
    # best_race_result = OutcomeResult()
    # best_progression_result = OutcomeResult()
    #
    # for grand_prix_name in grand_prix_names:
    #     predictor_totals, calculation_scores, predictor_totals = calculate_race_scores.calculate_race_scores(grand_prix_name, active_year, False)
    #     print("\n" + grand_prix_name)
    #     print("Qualifying", get_best_stage(GrandPrixStages.QUALIFYING, calculation_scores))
    #     print("Race", get_best_stage(GrandPrixStages.RACE, calculation_scores))
    #     print("Progession", get_best_stage(GrandPrixStages.PROGRESSION, calculation_scores))
    #     best_qualifying_result.add_outcome_result(get_best_stage(GrandPrixStages.QUALIFYING, calculation_scores))
    #     best_race_result.add_outcome_result(get_best_stage(GrandPrixStages.RACE, calculation_scores))
    #     best_progression_result.add_outcome_result(get_best_stage(GrandPrixStages.PROGRESSION, calculation_scores))
    #
    # print(best_qualifying_result)
    # print(best_race_result)
    # print(best_progression_result)

    summarise_season(active_year)
