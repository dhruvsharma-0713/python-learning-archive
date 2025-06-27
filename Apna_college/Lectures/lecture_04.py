info = {
    "name" : "Dhruvii",
    "age" : 21,
    "is_adult" : True,
    "subjects" : ["python", "C", "Java"],
    "topics" : ("dict", "set"),
}

print(type(info))
print(info)
print(info["name"])
print(info["topics"])

info["name"] = "Dhruv"
info["surname"] = "Sharma"
print(info)


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

#methods of sets

collection_2.add(1)
collection_2.add(2)
collection_2.add(3)
collection_2.add(4)
collection_2.add("hello")
collection_2.add("Dhruv Sharma")
collection_2.add("sets methods")

print(len(collection_2))
print(collection_2)


collection_2.remove(3)
collection_2.remove("sets methods")

print(len(collection_2))
print(collection_2)


collection_2.clear()

print(len(collection_2))
print(collection_2)


x = {"hello", "world", "coding", "python"}

print(x.pop())
print(x.pop())


print(collection.union(x))
print(collection.intersection(x))

print(collection)
print(x)
