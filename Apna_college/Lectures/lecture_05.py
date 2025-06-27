#loops in pyhton

count = 1
while count <= 10:
    print("hello world")
    count = count + 1 

# print numbers from 1 to 5

i = 1
while i <= 5:
    print(i)
    i += 1

print("loop ended")

# print numbers from 5 to 1

i = 5
while i >= 1:
    print(i)
    i -= 1

print("loop ended")


# break and continue

i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

print("loop ended")


i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1

print("loop ended")


#for loop and for loop with else 

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for val in nums:
    print(val)

veggies = ["potato", "tomato", "brinjal", "carrot"]

for val in veggies:
    print(val)
else:
    print("loop ended")


tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for val in tup: 
    print(val)

str = "dhruv sharma"

for char in str:
    print(char) 
else:
    print("loop ended")

#range in python

for i in range(1, 11):
    print(i)

for i in range(1, 11, 2):
    print(i)    


#pass statements in python

for i in range(1, 11):
    pass

print("loop ended")

if i > 5:
    pass

print("loop ended")

