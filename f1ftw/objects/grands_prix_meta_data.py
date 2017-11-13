from objects.collection_class import CollectionClass

class GrandsPrixMetaData(CollectionClass):
    def __init__(self):
        CollectionClass.__init__(self)
    def GetBeforeDate(self, date_value):
        filtered_results=GrandsPrixMetaData()
        for grand_prix_meta_data in self:
            if grand_prix_meta_data.end_date < date_value:
                filtered_results.AddObject(grand_prix_meta_data)
        return filtered_results
    def GetByName(self, grand_prix_name):
        filtered_results = [md for md in self if md.name == grand_prix_name]
        if len(filtered_results) == 1:
            return filtered_results[0]
        else:
            return None
    def GetNextGrandPrixMetaData(self,date_value):
        filtered_results = [md for md in self if md.end_date > date_value]
        filtered_results = sorted(filtered_results, key=lambda GrandPrixMetaData: GrandPrixMetaData.end_date)
        #need to sort by end date too
        if len(filtered_results) > 0:
            return filtered_results[0]
        else:
            return None
    def GetNames(self):
        names=[]
        for s in self:
            names.append(s.name)
        return names

class GrandPrixMetaData(object):
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
