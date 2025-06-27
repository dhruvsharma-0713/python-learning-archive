cities = ["Delhi", "Chandigarh", "Jaipur", "Mumbai","Bulandshahr","Dehradun"]
x = 10
y = 1307

#Write a function to print the lenght of the list. (list is the parameter)

def length_of_list(list):
    print(len(list))

length_of_list(cities)


#write a function to print the elements of a list in a single line. (list is the parameter)

def print_list(list):
    for i in list:
        print(i, end = " ")    
    print()

print_list(cities)


#write a function to find the factorial of a number n. (n is the parameter)

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

factorial(x)


#write a function to convert USD to INR.

def usd_to_inr(usd):
    inr = usd * 83.97
    print(inr)

usd_to_inr(y)


#write a function to print the multiplication table of a number n. (n is the parameter) 

def multiplication_table(n):
    for i in range(1, 11):
        print(n*i)

multiplication_table(x)


#write a function to identify a number is odd or even 

def odd_even(num):
    if(num % 2 == 0):
        print("The number you entered is an even number")
    else:
        print("The number you entered is an odd number")

odd_even(num = (int(input("enter number = "))))


#write a recursive function to calculate the sum of first n numbers. (n is the parameter)   

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
    
print(sum(n = int(input("enter number = "))))


#write a recursive function to print all elements in a list. HINT: use list and index as parameters.

def print_elements(list):
    if len(list) == 0:
        return
    else:
        print(list[0])
        print_elements(list[1:])

list = [23, 89, 74, 52, 94, 56, 77]
print_elements(list)


