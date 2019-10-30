import calculate_scores
import objects
from objects.collection_class import CollectionClass
import get_grand_prix_names
from get_predictors import GetPredictors
import load_config

class PredictorRaceWinTotals(CollectionClass):
    def __init__(self):
        CollectionClass.__init__(self)
    def IncrementWinTotalForPredictor(self, predictor):
        for item in self:
            if item.predictor == predictor:
                item.win_total += 1

class PredictorRaceWinTotal(object):
    def __init__(self, predictor):
        self.predictor = predictor
        self.win_total = 0
    def __str__(self):
        return "Predictor: " + str(self.predictor) + " Wins: " + str(self.win_total)

def setup_predictor_wins(active_year):
    predictor_wins = PredictorRaceWinTotals()
    predictors=GetPredictors(active_year)
    for predictor in predictors:
        predictor_wins.AddObject(PredictorRaceWinTotal(predictor))
    return predictor_wins

def calculate_race_win(grand_prix_name, active_year):
    calculation_scores = calculate_scores.calculate_race_score(grand_prix_name, active_year)
    predictor_totals = objects.predictor_totals.PredictorTotals()
    for calculation_score in calculation_scores:
        for calc_result in calculation_score.results:
            predictor_totals.AddOrUpdatePredictorTotalPoints(objects.predictor_totals.PredictorTotal(calc_result.predictor, calc_result.score))
    return sorted(predictor_totals, key = lambda x: x.points, reverse = True)

def display_race_win_totals(predictor_wins):
    print("\nTotal Race Wins by Predictor:\n")
    for predictor_win in predictor_wins:
        print(str(predictor_win.win_total) + "\t" + str(predictor_win.predictor))

def calculate_total_race_wins(active_year):
    grand_prix_names = get_grand_prix_names.get_grand_prix_names(active_year = active_year)
    predictor_wins = setup_predictor_wins(active_year)

    for grand_prix_name in grand_prix_names:
        predictor_totals = calculate_race_win(grand_prix_name, active_year)
        winning_total = predictor_totals[0].points
        for predictor_total in predictor_totals:
            if predictor_total.points == winning_total:
                predictor_wins.IncrementWinTotalForPredictor(predictor_total.predictor)
    predictor_wins = sorted(predictor_wins, key = lambda x: x.win_total, reverse = True)
    return predictor_wins

def calculate_race_wins(active_year):
    grand_prix_names = get_grand_prix_names.get_grand_prix_names(active_year = active_year)
    for grand_prix_name in grand_prix_names:
        predictor_totals = calculate_race_win(grand_prix_name, active_year)
        winning_total = predictor_totals[0].points
        for predictor_total in predictor_totals:
            if predictor_total.points == winning_total:
                print(grand_prix_name + " GP\t\t" + str(predictor_total.predictor) + "\t(" + str(len(predictor_totals)) + " predictors)")


if __name__ == '__main__':
    config = load_config.read_config()
    calculate_race_wins(config.current_year)
    wins = calculate_total_race_wins(config.current_year)
    display_race_win_totals(wins)
