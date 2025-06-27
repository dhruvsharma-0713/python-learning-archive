#WAP to input user's first name and print its length.

name = input("enter your name : ")
print("length of your name = ", len(name))

#WAP to find occurrence of '$' in a string.

str = "hi, $iam the $citizen of $uland$hahr having $99.$99"
print(str.count("$"))

#WAP using conditional statements to grade students based on their marks

name = input("enter your name : ")
marks = float(input("enter your marks = "))

if(marks >= 90):
    print("your grades : 'A'")
elif(90 > marks >= 80):
    print("your grades : 'B'")
elif(80 > marks >= 70):
    print("your grades : 'C'")
elif(70 > marks):
    print("your grades : 'D'")

#WAP to check if a number entered by the user is odd or even.

a = int(input("enter number = "))

if(a % 2 == 0):
    print("The number you entered is an even number")
else:
    print("The number you entered is an odd number")

#WAP to find the greatest of 3 numbers entered by the user.

a = int(input("first number = "))
b = int(input("second number = "))
c = int(input("third number = "))

if(a > b and a > c):
    print("greatest number is a, which is ", a)
elif(b > c and b > a):
    print("greatest number is b, which is ", b)
elif(c > a and c > b):
    print("greatest number is c, which is ", c)

#WAP to check if a number is a multiple of 7 or not.

a = int(input("number ="))

if(a % 7 == 0):
    print("yes the number you entered is a multiple of 7")
else:
    print("yes the number you entered is not a multiple of 7")
