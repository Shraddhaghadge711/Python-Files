#1
a = int(input ("your number"))

try:
    print(10/a)
    
except ZeroDivisionError:
    print("sorry you can't divide by 0")
    
print("ok i have done the division") 


#2
a = int(input("tell number"))
try:
    print(10/a)

except Exception as err:
    print(f"sorry there is an err as {err}")
    
    
#3
a = int(input("tell number"))
try:
    print(10/a)

except Exception as err:
    print(f"sorry there is an err as {err}")
    
else: 
    print("good there is no exception")
    
#4

a = int(input("tell number"))
try:
    print(10/a)

except Exception as err:
    print(f"sorry there is an err as {err}")
    
finally:
    print("no matter what, i'll run")
    
#5
age = int(input("tell age"))

try:
    
    if age<10 or age>18:
        raise ValueError("age must be between 10 and 18")
    else:
        print("wlc to the club")
  
except Exception as err:
    print("an error occured as {err}")  
    
print("club will start soon")