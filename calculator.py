def add(x, y):
    return x + y
print(add(5,6))
$ py.test test_add.py

def subtract(x, y):
    return x - y
print(subtract(5,6))
$ py.test test_subtract.py

def divide(x, y):
    if y ==0:
        result="Invalid value for denominator, cant't divide by 0!"
    else:
        result = x / y 
    return result
print(divide(30,6))
print(divide(5,0))
$ py.test test_divide.py


def multiply(x, y):
     return x * y
print(multiply(8, 6))
$ py.test test_multiply.py

def square(x):
    return x ** 2
print( square(3))
$ py.test test_square.py


def power(x, y):
    return x ** y
print(power(7, 7))
$ py.test test_power.py


def sqrt(x):
     if x < 0:
        return None  
    epsilon = 0.00001  
    guess = x / 2.0  
    while abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2.0
    return guess       
print(sqrt(3))
$ py.test test_sqrt.py


