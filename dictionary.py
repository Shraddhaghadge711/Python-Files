info= {
    "name": "shraddha",
    "age": 20,
    "city": "Delhi",
    "subjects": ["Math", "Science", "English"],
    "topics": ("dictionary", "list", "tuple"),
    "marks": 100
    
}
print(info)
print(type(info))
print(info["name"])

null_dict = {}
print(null_dict)

#nested dict
student = {
    "name": "shraddha",
    "subjects": {
        "Math": 90,
        "Science": 80,
        "English": 70
    }
}
print(student)