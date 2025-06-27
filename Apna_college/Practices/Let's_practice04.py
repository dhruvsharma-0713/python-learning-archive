#store following word meaning in a python dictionary:
#table:"a piece of furniture", "list of facts and figures"
#cat: "a small animal"

dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts and figures"]
}

print(dictionary)


#you are given a list of subjects for students. assume one classroom is required for 1 subject. how many classrooms are needed by all students.
#"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"

subjects = {
    "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
}

print("number of subjects : ", len(subjects))
print("classrooms needed : ", len(subjects))


#WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary and add one by one. use subject names as keys and marks as values.

marks = {}

a =int(input("Enter Python marks : "))
marks.update({"Python" : a})

b =int(input("Enter Javascript marks : "))
marks.update({"Javascript" : b})

c =int(input("Enter DAA marks : "))
marks.update({"DAA" : c})


print(marks)
print(type(marks))


#figure out a way to store 9 and 9.0 as seperate values in the set.(you can take help of built-in data types)

number = {}

number[9] = 9
number[9.0] = 9.0

print(number)

