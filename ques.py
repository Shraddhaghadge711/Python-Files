#first question

'''a= int(input("enter first number:   "))
b= int(input("enter second number:   "))
print("sum of two numbers is: ", a+b)'''

#2nd question

'''side =float(input("enter side of square:   "))
print("area of square is: ", side*side)'''

#3rd question

'''x= float(input("enter first number:   "))
y= float(input("enter second number:   "))

print("average of two numbers is: ", (x+y)/2)'''

#4th question

'''a= int(input("enter first number:   "))
b= int(input("enter second number:   "))
print("a>=b is: ", a>=b)'''

#5th : input first name and find length of name
'''name = input("enter name :   ")
print("length of name is : ", len(name))

#6th: occurence of $ 
str = "Hi$ my name is $ shraddha $"
print(str.count("$"))

#7th: if no. is odd or even
number = int(input("enter number:   "))

if(number%2 == 0):
    print("Even")
elif(number%2 != 0):
    print("Odd")
    
#8th: finding greatest of 3 no. by users

x = int(input("enter first number:   "))
y = int(input("enter second number:   "))
z = int(input("enter third number:   "))

if( x >= y and x>= z):
    print("first number is greatest")
elif( y >= x and y >= z):
    print("second number is greatest")
else:
    print("third number is greatest") 
    
 #9th: multiple of 7 or not
 
number = int(input("enter number: "))
if ( number%7 == 0):
    print("multiple of 7")   
else: 
    print("not multiple of 7")    
    
    
#10th: ask the user to enter names of 3 fav moives & store them in ls
movies = []
mov1 = input("enter first movie:   ")
mov2 = input("enter second movie:   ")
mov3 = input("enter third movie:   ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)   

#11th: check if list is palindrome or not
numbers = [1, 2, 3, 2, 1]
copy_list = numbers.copy()
copy_list.reverse()
if numbers == copy_list:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")


#12th: tuplecount
tuple = ("C", "D", "A", "A", "B", "B", "A")
print(tuple.count("A"))

#13th: sort values  in list above
tuple = ["C", "D", "A", "A", "B", "B", "A"]
tuple.sort()
print(tuple)


#Accept an integer

n= int(input("tell ur num"))

for i in range(n):
    print("hello world")
    
#print natural no. upto n

n = int(input("tell num"))

for i in range(1, n+1):
    print(i)    
    
#reverse loop from n to 1
n = int(input("tell num"))
for i in range(n, 0,-1):
    print(i)    
    
#print table

n = int(input("tell num"))

for i in range(n, n*10+1,n):
    print(i)
    
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")        

#sum up to n terms
n= int(input("tell num"))

sum = 0

for i in range(1,n+1):
    sum = sum + i
print(f"your sum is {sum}")    

# factorial of no.

n= int(input("tell num"))

fact = 1

for i in range(1,n+1):
    fact = fact * i
print(f"your factorial is {fact}")
'''

# print sum of all even and odd in range separately
# n=int(input("tell num :- "))
# even = 0
# odd = 0

# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
        
# print(f"your even and odd sum are {even},{odd} ")            

# n = int(input("tell num that you want factors of : "))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)

# ques. check if mo. is perfect or not 

# n= int(input("check if your number is perfect or not: "))
# sum = 0
# for i in range(1, n):
#     if n%i == 0:
#         sum = sum + i
# if sum == n:
#     print("perfect no.")
# else:
#     print("not a perfect no.") 


#ques: check if it's a prime no. or not

# n= (int(input("whether ur no. is prime or not:")))

# count = 0      
    
# for i in range(1,n+1):
#       if n%i == 0:   
#           count = count + 1
          
#           print(count)
          
# if count == 2:
#     print("prime no.")
# else:
#     print("not a prime no.")            
        
        
#ques: reverse a string w/o using in build function

# a = input("enter string:")

# b = input("enter 2nd string:")

# for i in range(len(a)-1,-1,-1):

#     b = b+(a[i])
# print(b)

# if b == a:
#     print("pallindrome")
# else:
#     print("not a pallindrome")
    
    
#ques: count all letters, digits and special characters in a string

# n = input("enter ur string: ")

# char = 0
# digit = 0
# spchr = 0

# for i in n:

#     if i.isdigit():
#         digit += 1

#     elif i.isalpha():
#         char += 1

#     else:
#         spchr += 1

# print("Characters:", char)
# print("Digits:", digit)
# print("Special characters:", spchr) 

    
