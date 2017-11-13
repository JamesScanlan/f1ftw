class CalculationScoreResults(object):
    def __init__(self,stage):
        self.stage=stage
        self.results=None

class CalculationScoreResult(object):
    def __init__(self, predictor, score):
        self.predictor=predictor
        self.score=score
        self.log=None
    def __str__(self):
        return "Predictor: " + str(self.predictor) + " Score: " + str(self.score)
