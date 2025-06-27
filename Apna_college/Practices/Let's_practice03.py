#WAP to ask the user to enter names of their 3 favorite movies and store them in a list

favorite_movies = []
mov1 = input("enter name of your favorite movie 1: ")
mov2 = input("enter name of your favorite movie 2: ")
mov3 = input("enter name of your favorite movie 3: ")

favorite_movies.append(mov1)
favorite_movies.append(mov2)
favorite_movies.append(mov3)

print(favorite_movies)

#WAP to check if a list contains a palindrome of elements. (hint: use copy() method)     [1, 2, 3, 2, 1]     [1, 2, 3, 1]     [1, "abc", "abc", 1]

list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3, 1]
list3 = [1, "abc", "abc", 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrone")
else:
    print("Non Palandrone")

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("Palindrone")
else:
    print("Non Palandrone")

copy_list3 = list3.copy()
copy_list3.reverse()

if(copy_list3 == list3):
    print("Palindrone")
else:
    print("Non Palandrone")

#WAP to count the number of students with the "A" grade in the following tuple.     ["C", "D", "A", "A", "B", "B", "A"]

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

#WAP to store the above values in a list and sort them from "A" to "D".

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)
