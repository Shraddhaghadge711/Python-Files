class Factory:
    a = 12 #attribute
    
    def hello(self): #method
        print("how are u?")
        
    print("how r u and i'm getting initialized")
    
Factory()
print(Factory().a)

Factory().hello()

    
    
    