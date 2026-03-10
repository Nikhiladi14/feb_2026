'''Write a Python function square_all(numbers) that takes a list of numbers as input
and returns a new list containing the square of each number in the input list.
Use the map() function with a lambda function to implement this.'''

def square_all(numbers):
    return list(map(lambda x:x**2, numbers))
nums = [2, 5, 6, 4, 12] 
result = square_all(nums)
print(result)

'''Write a Python function filter_positive(numbers) that takes a list of numbers as
input and returns a new list containing only the positive numbers from the
input list. Use the filter() function with a lambda function to implement this.'''

def filter_positive(numbers):
    return list(filter(lambda x:x>0,numbers))
List_1 = [-5, 25, -2, 12, -10, 1, -3]
result = filter_positive(List_1)
print(result)

'''Write a Python function calculate_factorial(n) that calculates the factorial 
of a given number n . Use the reduce() function with an a
ppropriate lambda function to implement this. '''

from functools import reduce

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))

print(calculate_factorial(5))

'''Write a Python function count_vowels(string) that takes a string as input 
and returns the count of vowels (a, e, i, o, u) in the input string. Use the 
reduce() function with an appropriate lambda function to implement this. '''
from functools import reduce

def count_vowels(string):
    vowels = "aeiouAEIOU"
    return reduce(lambda count, char: count + 1 if char in vowels else count, string, 0)
print(count_vowels("Hello World"))