# a = [12,13,14,15,16,34.5]

# #1st way using index

# for i in range(len(a)):
#     print(a[i])
    
    
# #2nd way directly on values

# for i in a:
#     print(i)    


# l = [1,3,4,5]

# l.append(6)
# print(l)

# l.insert(1,2)
# print(l)

#ques. print first pos and neg

# l = [-45,67,12,-68,-69,34]

# print("positive elements are ")
# for i in l: 
#     if i>=0:
#         print(i)
# print("negative elements are")

# for i in l:
#     if i<0:
#         print(i)

#ques. average of list elements

# l = [12,345,53,68,99,25]

# sum = 0

# for i in l:
#     sum = sum+i
# print(sum/len(l))

#ques. great no. and print its index

# l = [12,345,53,68,99,25]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i
# print(f"largest no. is {largest} and its index is {index}")
    
#ques

# l = [12,16,13,19]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i> largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i
        
# print(sec_largest, largest)

#check if l is sorted or not

# l = [10,11,12,13,14,15]

# for i in range(len(l)):
#     if l[i] < l[i +1]:
#         continue
#     else:
#         print("list is not sorted")
#         break
# else:
#     print("list is sorted")
    