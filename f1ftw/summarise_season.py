import get_grand_prix_names
import calculate_race_scores
import load_config
import datetime
from objects.grand_prix_stages import GrandPrixStages

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

def get_best_stage(grand_prix_stage):
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

if __name__== "__main__":
    config = load_config.read_config()
    active_year = datetime.date.today().year
    grand_prix_names = get_grand_prix_names.get_grand_prix_names(datetime.date.today(), active_year)

    best_qualifying_result = OutcomeResult()
    best_race_result = OutcomeResult()
    best_progression_result = OutcomeResult()

    for grand_prix_name in grand_prix_names:
        predictor_totals, calculation_scores, predictor_totals = calculate_race_scores.calculate_race_scores(grand_prix_name, active_year, False)
        # print("\n" + grand_prix_name)
        # print("Qualifying", get_best_stage(GrandPrixStages.QUALIFYING))
        # print("Race", get_best_stage(GrandPrixStages.RACE))
        # print("Progession", get_best_stage(GrandPrixStages.PROGRESSION))
        best_qualifying_result.add_outcome_result(get_best_stage(GrandPrixStages.QUALIFYING))
        best_race_result.add_outcome_result(get_best_stage(GrandPrixStages.RACE))
        best_progression_result.add_outcome_result(get_best_stage(GrandPrixStages.PROGRESSION))

    print(best_qualifying_result)
    print(best_race_result)
    print(best_progression_result)
