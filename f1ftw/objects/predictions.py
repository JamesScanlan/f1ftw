from objects.text_layout import FormatItem

class QualifyingPrediction(object):
    def __init__(self,driver):
        self.driver=driver
    def __repr__(self):
        return "{}:\n\t{}".format(self.__class__.__name__,self.driver.person_name,self.driver.team)
    def __eq__(self,other):
        return self.driver == other.driver
    def __str__(self):
        return str(self.driver)
##have you heard of object orientation and inheritance?

class RacePrediction(object):
    def __init__(self,driver):
        self.driver=driver
    def __repr__(self):
        return "{}:\n\t{}".format(self.__class__.__name__,self.driver.person_name,self.driver.team)

class ProgressionPrediction(object):
    def __init__(self,team):
        self.team=team
    def __str__(self):
        return self.team
    def __repr__(self):
        return "{}:\n\t{}".format(self.__class__.__name__,self.team)

class JokerPrediction(object):
    def __init__(self,team):
        self.team=team
    def __repr__(self):
        return "{}:\n\t{}".format(self.__class__.__name__,self.team)

class Prediction(object):
    def __init__(self, grand_prix, predictor, qualifying_prediction, race_prediction, progression_prediction, joker_prediction):
        self.grand_prix = grand_prix
        self.predictor = predictor
        self.qualifying_prediction = qualifying_prediction
        self.race_prediction = race_prediction
        self.progression_prediction = progression_prediction
        self.joker_prediction = joker_prediction
    def __str__(self):
        return FormatItem(str(self.grand_prix),15) + "\t" + FormatItem(str(self.predictor),20) + "\t" + FormatItem(str(self.qualifying_prediction),20) + "\t" + FormatItem(str(self.race_prediction),20) + "\t" + FormatItem(str(self.progression_prediction),15) + "\t" + str(self.joker_prediction)
