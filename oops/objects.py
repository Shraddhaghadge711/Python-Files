class Factory:
    a = 12
    
    def hello(self):
        print("how are u?")
        
    print("how r u and i'm getting initialized")
    
obj = Factory()

obj.hello()


print(obj.a)
