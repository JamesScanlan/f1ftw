import sys
from objects.collection_class import CollectionClass

class CommandLineArguments(CollectionClass):
    def __init__(self):
        CollectionClass.__init__(self)
        self.ReadCommandLine()
    def ReadCommandLine(self):
        for argumentCounter in range(1,len(sys.argv)):
            self.AddObject(sys.argv[argumentCounter])
