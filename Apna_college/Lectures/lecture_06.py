#functions and recursion in python 

a = 10
b = 20

sum = a + b
print(sum)

#more lines of code 

a = 39
b = 40

sum = a + b
print(sum)

#more lines of code 

a = 87
b = 43

sum = a + b
print(sum)

def calc_sum(a, b):
    sum = a + b
    return sum

print(calc_sum(10, 20))

#now using function

calc_sum(10, 20)
calc_sum(39, 40)
calc_sum(87, 43)

#for more lines of code

def calc_sum(a, b):
    return a + b

sum = calc_sum(10, 20)
print(sum)

#average of 3 numbers

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    return avg

avg = calc_avg(10, 20, 30)
print(avg)


#recursion in python

def show(n):
    if(n == 0):
        return
    print(n)
    show(n - 1)

show(10)

#return n!

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n - 1)
    
print(fact(5))

