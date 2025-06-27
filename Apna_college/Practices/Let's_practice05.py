#print numbers from 1 to 100.

number = 1
while number <= 100:
    print(number)
    number += 1


#print numbers from 100 to 1.

number = 100
while number >= 1:
    print(number)
    number -= 1


#print the multiplication table of a number n.

n = int(input("Enter a number : "))
x = 1

while x <= 10:
    print(n*x)
    x += 1


#print the elements of the following list using loops: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 1
while i <= 10:
    print(i)
    i += 1

#or we can also solve tlike this....

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1


#search for a number x in this tuple using loop: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter a number : "))

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
    i += 1

 
#print the elements of the following list using loops: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] #using for loop

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for val in nums:
    print(val)  


#search for a number x in this tuple using loop: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) #using for loop

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter a number : "))

idx = 0
for val in nums:
    if(val == x):
        print("FOUND at idx", idx)
    idx += 1


#using for and range() function
# (i) print numbers from 1 to 100.
# (ii) print numbers from 100 to 1.
# (iii) print the multiplication table of a number n.

# (i)

for i in range(1, 101):
    print(i) 

#(ii)

for i in range(100, 0, -1):
    print(i)

#(iii)

n = int(input("Enter a number : "))

for i in range(1, 11):
    print(n*i)


#WAP to find the sum of first n numbers. (using for while loop)

n = int(input("Enter a number : "))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(sum)


#WAP to find the factorial of first n numbers. (using for loop)

n = int(input("Enter a number : "))

fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)


