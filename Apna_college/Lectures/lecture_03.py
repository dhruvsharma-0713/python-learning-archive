#list

student = ["dhruv", 95.7, 21, "bulandshshr"]
print(student)
student[0] = "dhruv sharma"
print(student)

#slicing in list

marks = [85, 94, 76, 63, 48]
print(marks[1:4])
print(marks[:4])
print(marks[1:])

#methods for list

list = [2, 1, 3]
list.append(4)      #adds one element at the end

print(list)
print(list.sort())     #sorts in ascending order
print(list)
print(list.sort(reverse=True))     #sorts in decending order
print(list)
list.reverse()     #reverses list
print(list)
list.insert(1, 5)     #insert element at index
print(list)
list.remove(5)     #removes first occurrence of element
print(list)
list.pop(2)     #removes element at idx
print(list)

#Tuples in Python

tup = (3, 1, 2, 4)
print(type(tup))
print(tup)

#tuple methods

tup = (3, 1, 2, 4, 1)

print(tup.index(1))     #returns index of first occurrence
print(tup.count(1))     #counts total occurrences
