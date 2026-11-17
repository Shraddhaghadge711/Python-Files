class Animal:
    def show(self):
        print("I am an animal")
 
 
#this is method overriding in polymorphism       
class Human(Animal):
    def show(self):
        print("I am a human")
        
obj = Human()
obj.show()


#duck typing in polymorphism

class Animal:
    def show(self):
        print("I am an animal")
        
class Human:
    def show(self):
        print("I am a human")
        
obj = Animal()
obj2 = Human()
obj.show()
obj2.show()