"""Write a Python function named add that takes two arguments a and b and
returns their sum."""


def add(a,b):
    return a + b
result = add(10,20)
print("The addition value is :", result)

""""Write a Python function named square that takes a number x as input and
returns its square."""
def square(x):
    return x*x
result = square(4)
print("The sqaure value is:",result)

''''Write a Python function named factorial that takes a positive integer n as
input and returns its factorial.
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else :
        return n * factorial(n-1)
num = int(input("Enter number :"))
result = factorial(num)
print("The Factorial number is :", result)


'''Write a Python function named maximum that takes a list of numbers as input and
returns the maximum value in the list.
'''

def maximum(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
    
nums = [10, 20, 55, 30, 78,]
print("maximum value is :",maximum(nums))


'''Write a Python function named reverse that takes a string s as input and
returns its reverse.'''

def reverse(s):
    return s[::-1]
__name__ = "Pythonlife"
print("The reverse string is :",reverse(__name__))

'''Write a Python function named is_prime that takes a positive integer n as input
and returns True if n is prime, otherwise False .
'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % 2 == 0:
            return False
    return True
obj = int(input("Enter a number :"))

if obj % 2 == 0:
    print("Given number is Not Prime")
else :
    print("Given number is prime :", obj)


'''Write a Python function named fibonacci that takes a positive integer n as
input and returns the n th Fibonacci number.
'''

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a,b = 0,1
    for i in range(3, n+1):
        a,b = b,a+b
    return b

num = int(input("Enter number:"))
print("The",num,"th fibonacci number is:",fibonacci(num))


'''Write a Python function named is_palindrome that takes a string s as input and
returns True if s is a palindrome, otherwise False .
'''
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))  
print(is_palindrome("hello"))

'''Write a Python function named sum_of_squares that takes a list of numbers as
input and returns the sum of the squares of those numbers.
'''

def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num * num
    return total
nums = [2, 3, 4]
print(sum_of_squares(nums))

'''Write a Python function named average that takes a list of numbers as input and
returns the average value'''

def average(numbers):
    if len(numbers) == 0:
        return 0
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
nums = [10, 20, 30, 40]
print(average(nums))