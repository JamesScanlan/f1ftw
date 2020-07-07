import sys
from objects.collection_class import CollectionClass

class CommandLineArguments(CollectionClass):
    def __init__(self):
        CollectionClass.__init__(self)
        self.read_command_line()
    def read_command_line(self):
        for argumentCounter in range(1,len(sys.argv)):
            self.add_object(sys.argv[argumentCounter])

class CommandLineArgumentsProcessor(object):
    def __init__(self):
        self.command_line_arguments = CommandLineArguments()
    def get_argument(self, index):
        if isinstance(index, int) == False:
            return None
        if len(self.command_line_arguments) == 0:
            return None
        if index > len(self.command_line_arguments):
            return None
        if index < 0:
            return None
        return self.command_line_arguments[index]
    def __len__(self):
        return len(self.command_line_arguments)
