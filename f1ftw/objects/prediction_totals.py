from objects.collection_class import CollectionClass

class PredictionTotals(CollectionClass):
    def __init__(self):
        super().__init__()
    def add_or_update_prediction_total(self, prediction_total):
        self[self.upsert_object(prediction_total)].count += 1
    def add_prediction_total(self, prediction_total):
        prediction_total.count = self.GetInstanceCount(prediction_total) + 1
        self.add_object(prediction_total)
    def get_instance_count(self, prediction_total):
        count = 0
        for total in self:
            if total == prediction_total:
                count +=1
        return count
