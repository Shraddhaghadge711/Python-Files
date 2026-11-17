str1 = "This is a string.\nWe can use single or double quotes to define a string."
str2 = 'This is another string.\t myself shraddha'
str3 = '''This is a multi-line string.'''

print(str1)
print(str2)
print(str3) 

# concatination of strings
str4 = "Sarvesh"
print(len(str4))
str5 = "shraddha"

print(str4 + "  " + str5)

#indexing of strings

str6 = "Python"
ch = str6[1]
print(ch)

#slicing of strings

str7 = "Python Programming"
print(str7[0:4])
print(str7[:4]) #{0,1,2,3}
print(str7[5:]) #[5:len(str7)]

str8= "python Programming"
print(str8.endswith("amm")) #returns True if string ends with "amm"
print(str8.capitalize()) #converts first character to uppercase
print(str8.replace("python", "java")) #replaces all occurrences of "python" with "java"
print(str8.find("o")) #index of first occurrence of o
print(str8.count("o")) #count of occurrences of o

