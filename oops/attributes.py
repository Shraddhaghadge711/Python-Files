class Animal:
    
    name = "lion"
    
    def __init__(self):
        self.age = age #instance attribute
        
    def show(self): #instance method
        print("how r u")
        
    @classmethod
    def hello(cls):
        print("hii how r u bruh")
        
    @staticmethod
    def static():
        print("this is static method")
        
obj = Animal()
    
        
        
        