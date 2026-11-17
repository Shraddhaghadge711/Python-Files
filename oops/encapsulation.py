class Factory:
    _a = "pune"
    
#to protect the data we use underscore before the variable name
    def show(self):
        print("hello i'm in pune factory")

class Bhopal(Factory):
    def show2(self):
        print(super()._a)
        
obj = Bhopal()
obj.show2()

#private attributes and methods in encapsulation

print("private attributes and methods in encapsulation can be shown by using double underscore before the variable name")

class Demo:
    def __init__(self):
        self.name = "Shraddha"       #public attribute
        self._age = 100             #protected attribute
        self.__salary = 1000000     #private attribute
        
def show(self):
    print("inside the class:")
    print("public attribute:",self.name)
    print("protected attribute:",self._age)
    print("private attribute:",self.__salary)   