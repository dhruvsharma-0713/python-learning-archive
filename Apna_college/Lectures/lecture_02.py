str1 = "This is a string."
str2 = 'This is also a string'
str3 = """this is a string too"""

str = "This is a string.\nwe are creating it in python."
print(str)

str = "This is a string.\twe are creating it in python."
print(str)

str_a = "Dhruv"
len1 = len(str_a)
print(len1)
str_b = "Sharma"
len2 = len(str_b)
print(len2)

final_str = str_a + str_b

final_str1 = str_a + " " + str_b
len3 = len(final_str1)
print(len3)

print(str_a + str_b)
print(final_str)

#string and slicing

str = "dhruv sharma"
print(str[4])
print(str[1:6])
print(str[4:])
print(str[:6])

str = "apple"
print(str[-5:-1])

#conditional statements

age = int(input("Enter your age = "))

if(age >= 18):
    print("can vote and apply for license")
    print("can drive")

light = input("Enter colour of light = ")

if(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")
elif(light =="red"):
    print("stop")
else:
    print("Light is broken")

#nesting

name = input("enter your name : ")
age = int(input("enter your age : "))

if(age >= 18 ):
    if(age > 80 ):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("can drive")

