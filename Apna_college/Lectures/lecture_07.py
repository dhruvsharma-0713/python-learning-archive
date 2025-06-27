#nested dictionaries

student = {
    "name" : "Dhruv Sharma",
    "admission no" : "22SCSE1550018",
    "subjects" : {
        "DAA" : "78.5",
        "Python" : "97.4",
        "DBMS" : "98.3",
    },
}

print(student["name"])

student.update({"city" : "Bulandshahr"})
print(student)

#sets in python

collection = {1, 2, 2, 2, "hello", "world", 13}

print(collection)
print(type(collection))

collection_1 = {}
collection_2 = set()

print(type(collection_1))
print(type(collection_2))

#character introduction

character = {
    "name" : "Dhruv Sharma",
    "age" : 21,
    "is_adult" : True,
    "subjects" : ["python", "C", "Java"],
    "topics" : ("dict", "set"),
}

print(type(character))
print(character)
print(character["name"])
print(character["topics"])

character["name"] = "Dhruv"
character["surname"] = "Sharma"
print(character)

null_dict = {}
null_dict["name"] = "Dhruv"     #adds values to the dict
print(null_dict)

#nested dictionaries

student = {
    "name" : "Dhruv Sharma",
    "admission no" : "22SCSE1550018",
    "subjects" : {
        "DAA" : "78.5",
        "Python" : "97.4",
        "DBMS" : "98.3",
    },  
    "city" : "Bulandshahr"
}

print(student["name"])