#dunder methods
#stats and ends with double underscores

class Demo:
    def __init__(self):
        self.name = "Shraddha"
        self.age = 100
        
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def __add__(self,other):
        sum = 0
        for i in other:
        return f"Name: {self.name}, Age: {self.age} and Name: {other.name}, Age: {other.age}"
        return f"your sum of ages are {self.age + sum}"
    
obj = Demo()
obj2 = Demo()
print(obj)
print(obj + obj2)