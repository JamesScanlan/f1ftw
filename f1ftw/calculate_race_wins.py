import calculate_scores
import objects
from objects.collection_class import CollectionClass
import get_grand_prix_names
from get_predictors import GetPredictors

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

def SetupPredictorWins():
    predictor_wins = PredictorRaceWinTotals()
    predictors=GetPredictors()
    for predictor in predictors:
        predictor_wins.AddObject(PredictorRaceWinTotal(predictor))
    return predictor_wins

def CalculateRaceWin(grand_prix_name):
    calculation_scores = calculate_scores.CalculateRaceScore(grand_prix_name)
    predictor_totals = objects.predictor_totals.PredictorTotals()
    for calculation_score in calculation_scores:
        for calc_result in calculation_score.results:
            predictor_totals.AddOrUpdatePredictorTotalPoints(objects.predictor_totals.PredictorTotal(calc_result.predictor, calc_result.score))
    return sorted(predictor_totals, key = lambda x: x.points, reverse = True)

def DisplayRaceWinTotals(predictor_wins):
    print("\nTotal Race Wins by Predictor:\n")
    for predictor_win in predictor_wins:
        print(str(predictor_win.win_total) + "\t" + str(predictor_win.predictor))

def CalculateTotalRaceWins():
    grand_prix_names = get_grand_prix_names.GetGrandPrixNames()
    predictor_wins = SetupPredictorWins()

    for grand_prix_name in grand_prix_names:
        predictor_totals = CalculateRaceWin(grand_prix_name)
        if len(predictor_totals) >0:
            predictor_wins.IncrementWinTotalForPredictor(predictor_totals[0].predictor)
    predictor_wins = sorted(predictor_wins, key = lambda x: x.win_total, reverse = True)
    return predictor_wins

def CalculateRaceWins():
    grand_prix_names = get_grand_prix_names.GetGrandPrixNames()
    for grand_prix_name in grand_prix_names:
        predictor_totals = CalculateRaceWin(grand_prix_name)
        if len(predictor_totals) >0:
            print(grand_prix_name + " GP\t\t" + str(predictor_totals[0].predictor) + "\t(" + str(len(predictor_totals)) + " predictors)")

if __name__ == '__main__':
    CalculateRaceWins()
    wins = CalculateTotalRaceWins()
    DisplayRaceWinTotals(wins)
