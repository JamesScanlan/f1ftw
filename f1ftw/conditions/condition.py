class Condition(object):
    def __init__(self, function, message):
        self.function = function
        self.message = message
    def Evaluate(self):
        return self.function
