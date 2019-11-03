import sys
from objects.collection_class import CollectionClass

class CommandLineArguments(CollectionClass):
    def __init__(self):
        CollectionClass.__init__(self)
        self.read_command_line()
    def read_command_line(self):
        for argumentCounter in range(1,len(sys.argv)):
            self.add_object(sys.argv[argumentCounter])
