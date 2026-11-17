# #for loop
# a = range(1,20,2)

# for i in a:
#     print(i)

# #14th: reverse loop of 20 to 50, 16 to 1, -3 to -15

# for i in range(20,51,1):
#     print(i)
    
# for i in range(16,0,-1):
#     print(i)    

# for i in range(-3,-16,-1): 
#     print(i)   
    
# #printing table of 5

# for i in range(5, 51, 5):
#     print(i)
    
# #print table of n num

# n= int(input("table uh want"))
# for i in range(n, n*10+1,n ):
#    print(i)       
    
# a = "SHERYIANS"

# for i in range(9):
#     print(a[i])    
# print(len(a))

# a= "shraddha is cool"
# for i in a:
#     print(i)
    
# for i in range(1,21):
#     if i==15:
#         break
#     else:
#         print(i)
        
# for i in range(2,35,1):
#     if i==35:
#         print("break is executed")
#         break
#     print(i)
    
# else:
#     print("break is not executed")            

# a = 1

# while a <= 30:
#     print(a)
#     a = a +1

#ques: while loop

# a =int(input("tell no."))

# while a>0:
#     print(a%10)
#     a= a//10

#ques. reverse no.

# a =int(input("tell no."))

# rev = 0

# while a>0:
#     rev = rev*10 + a%10
#     a= a//10
# print(rev)    

#ques: check if no. is pallindrome or not
# a =int(input("tell no."))
# copy = a 
# rev = 0

# while a>0:
#     rev = rev*10 + a%10
#     a= a//10


# if copy == rev:
#     print("pallindrome")
# else:
#     print("not pallindrome")   



#create a random no. guessing game using python 

  
import random

num = random.randint(1,10)

tries = 0

while True:
    guess = int(input("guess the no. between 1 to 10 :- "))
    tries += 1
    if guess < num:
        print("too low")
    elif guess > num:
        print("too high")
    else:
        print(f"you guessed it right in {tries} tries")
        break
    
    
    
      

