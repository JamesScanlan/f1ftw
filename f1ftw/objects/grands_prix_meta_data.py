from objects.collection_class import CollectionClass

class GrandsPrixMetaData(CollectionClass):
    def __init__(self):
        CollectionClass.__init__(self)

    def __str__(self):
        for s in self:
            print(s)

    def get_before_date(self, date_value):
        filtered_results=GrandsPrixMetaData()
        for grand_prix_meta_data in self:
            if grand_prix_meta_data.end_date < date_value:
                filtered_results.add_object(grand_prix_meta_data)
        return filtered_results

    def get_before_previous_or_current_race_weekends(self, date_value):
        filtered_results = GrandsPrixMetaData()
        for grand_prix_meta_data in self:
            if grand_prix_meta_data.end_date <= date_value:
                filtered_results.add_object(grand_prix_meta_data)
        return filtered_results

    def get_by_name(self, grand_prix_name):
        filtered_results = [md for md in self if md.name == grand_prix_name]
        if len(filtered_results) == 1:
            return filtered_results[0]
        else:
            return None

    def get_next_grand_prix_meta_data(self,date_value):
        filtered_results = [md for md in self if md.end_date > date_value]
        filtered_results = sorted(filtered_results, key=lambda GrandPrixMetaData: GrandPrixMetaData.end_date)
        #need to sort by end date too
        if len(filtered_results) > 0:
            return filtered_results[0]
        else:
            return None

    def get_names(self):
        names=[]
        for s in self:
            names.append(s.name)
        return names

class GrandPrixMetaData(object):
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
    def __str__(self):
        return self.name + " " + str(self.start_date) + " " + str(self.end_date)
