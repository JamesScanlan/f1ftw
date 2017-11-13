#from condition import Condition
import inspect

class Hello(object):
    def SaySomething(self, name):
        print("Hello " + name)
        return True

class Goodbye(object):
    def SaySomething(self, name):
        print("Bye bye " + name)
        return False

def SayMonkey(word):
    print(word)
    return "Monkey"

class Caller(object):
    def __init__(self, function_call):
        self.function_call = function_call
    def CallFunction(self):
        return lambda: self.function_call()

#class_a = Hello()
#class_b = Goodbye()
#print(callable(SayMonkey()))

#Condition Route
#condition = Condition(SayMonkey("Llama"),"Monkey")
#thing=condition.Evaluate()

caller = Caller(SayMonkey("Shark"))
thing = caller.CallFunction()

print(inspect.isfunction(thing))
print(inspect.getmembers(thing))
print(thing)


#condition=Condition(class_a.SaySomething("James"),"What")
#print(condition.Evaluate())
#if condition.Evaluate() == True:
#    print("It was TRUE")
#else:
#    print("It was so not TRUE")
