from objects.collection_class import CollectionClass

class PredictorTotals(CollectionClass):
    def __init__(self):
        CollectionClass.__init__(self)
    def GetPredictorIndex(self, predictor):
        index = 0
        for predictor_total in self.objects:
            if predictor_total.predictor == predictor:
                return index
            else:
                index += 1
        return -1
    def AddPredictorTotal(self, predictor_total):
        self.AddObject(predictor_total)
    def AddOrUpdatePredictorTotalPoints(self, predictor_total):
        index=self.GetPredictorIndex(predictor_total.predictor)
        if index > -1:
            self.objects[index].points += predictor_total.points
        else:
            self.AddPredictorTotal(predictor_total)
    def AppendPredictorTotalPoints(self, predictor, points):
        index = self.GetPredictorIndex(predictor)
        if index > -1:
            self.objects[index].points += points
        else:
            self.AddPredictorTotal(PredictorTotal(predictor,points))

class PredictorTotal(object):
    def __init__(self,predictor,points):
        self.predictor=predictor
        self.points=points
    def __eq__(self,other):
        return self.predictor == other.predictor
    def __str__(self):
        return "Predictor: " + str(self.predictor) + " Points: " + str(self.points)
