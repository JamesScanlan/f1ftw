import objects
from collection_class import CollectionClass

class Thing(object):
    def __init__(self,name):
        self.name=name

class TestObject(CollectionClass):
    def __init__(self):
        CollectionClass.__init__(self)
    def AddThing(self, object):
        CollectionClass.AddObject(self, object)

t=TestObject()
t.AddObject("Cat")
t.AddThing("Dog")

print("There are " + str(len(t)) + " objects in t")

print("Finished")
