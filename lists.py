marks = [98.43, 67.9, 87.23, 80.61]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0]) 

student = ["shraddha", 85, "Beed"]
print(student)
student[0] = "Shruu"
print(student)

marks = [88, 66, 84, 32, 75]
print(marks[1:4])
marks.append(56)
print(marks)
marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)

marks.insert(2,99)
print(marks)

marks.remove(66)
print(marks)

marks.pop(2)
print(marks)