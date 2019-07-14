from objects.collection_class import CollectionClass

class Drivers(CollectionClass):
    def __init__(self):
        CollectionClass.__init__(self)
    def Sort(self):
        self.objects.sort(reverse = False, key=lambda x:(x.team, x.person_name.last_name))
