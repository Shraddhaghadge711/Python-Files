class Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
        
    def show(self):
        print(f"your object details are {self.material}")
    
reebok = Factory("leather",3,2)

campus = Factory("nylon",2,3)

print(reebok.material)
print(campus.zips)

reebok.show()
campus.show()

