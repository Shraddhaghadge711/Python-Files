age = 21

if(age> 21):
    print("can vote and apply for license")
elif(age<= 18):
    print("cannot vote")  
elif(age>=18):
    print("can vote but cannot apply for license")    
    
else:
    print("invalid age")    
    
#grade 
marks = int(input("Enter your marks: "))
if(marks>=90):
    print("A grade")
elif(90>marks>=80):
    print("B grade")
elif(marks>=70 and marks<80):
    print("C grade")
elif(70>marks):
    print("D grade")
else:
    print("Failed")            
    
    
#nesting   

age = int(input("Enter your age: "))

if(age >= 18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")        
    