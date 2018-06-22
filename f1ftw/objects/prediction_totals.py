from objects.collection_class import CollectionClass

class PredictionTotals(CollectionClass):
    def __init__(self):
        super().__init__()
    def AddOrUpdatePredictionTotal(self, prediction_total):
        self[self.UpsertObject(prediction_total)].count += 1
    def AddPredictionTotal(self, prediction_total):
        prediction_total.count = self.GetInstanceCount(prediction_total) + 1
        self.AddObject(prediction_total)
    def GetInstanceCount(self, prediction_total):
        count = 0
        for total in self:
            if total == prediction_total:
                count +=1
        return count
