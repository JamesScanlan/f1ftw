from objects.collection_class import CollectionClass

class PredictorTotals(CollectionClass):
    def __init__(self):
        CollectionClass.__init__(self)
    def get_predictor_index(self, predictor):
        index = 0
        for predictor_total in self.objects:
            if predictor_total.predictor == predictor:
                return index
            else:
                index += 1
        return -1
    def add_predictor_total(self, predictor_total):
        self.add_object(predictor_total)
    def add_or_update_predictor_total_points(self, predictor_total):
        index = self.get_predictor_index(predictor_total.predictor)
        if index > -1:
            #print(predictor_total.points)
            self.objects[index].points += predictor_total.points
        else:
            self.add_predictor_total(predictor_total)
    def append_predictor_total_points(self, predictor, points):
        index = self.get_predictor_index(predictor)
        if index > -1:
            self.objects[index].points += points
        else:
            self.add_predictor_total(PredictorTotal(predictor, points))

class PredictorTotal(object):
    def __init__(self,predictor,points):
        self.predictor=predictor
        self.points=points
    def __eq__(self,other):
        return self.predictor == other.predictor
    def __str__(self):
        return "Predictor: " + str(self.predictor) + " Points: " + str(self.points)
