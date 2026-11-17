class Factorymumbai:
    
    a = "an attribute mentioned inside Factory"
    
    def hello(self):
        print("how are u?")
        
class Factorypune(Factorymumbai): #child class
    pass

obj = Factorymumbai()

obj2 = Factorypune()

print(obj.a)

print(obj2.hello())
        
#constructor in inheritance

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"your object details are {self.name} and {self.age}")
        
class Human(Animal):
    pass

person1 = Human("Shraddha",86)
person2 = Human("Shruti",90)

person1.show()
person2.show()

#multiple inheritance

class Animal:
    def __init__(self):
        self.name1 = "Lion"
    
class Human:
    def __init__(self):
        pass
    name2 = "Shraddha"
    
class Robots(Animal,Human):
    name3 = "charlie123"
    
obj = Robots()

print(obj.name1)
    
#multilevel inheritance

class Factory: #grandparent class
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips
        
class BhopalFactory(Factory): #parent class
    def __init__(self, material,zips,color):
        super().__init__(material,zips)
        self.color = color
        
class PuneFactory(BhopalFactory): #child class
    def __init__(self,material,zips,color,price):
        super().__init__(material,zips,color)
        self.price = price
        
obj = PuneFactory("cotton", 10, "blue", 100)