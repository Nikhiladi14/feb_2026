# 1. Print Statement: Write a Python program that prints your name.
print("Nikhil adi")

# 2. Comments: Create a pyhton script with both single-line & multi-line comments explaining the purpose of the script
# In the below code, we take two numbers and perform subtraction operation.
num_1 = 923
num_2 = 810
result = num_1 - num_2
print(result) 
'''
A variable num_1 contains value 923
A variable num_2 contains value 810
in the result we perform subtraction operation & result is used to display output
'''
# 3. Data Structures & Data Types: Define a list containing three different data types
list = [35, 5.7, "python", [1,2,3]]
print(list)

# Define a set containing employee id's.
employee_id = {559, 660, 661, 662} 
print(employee_id)

# 4. String Operations: Concatenate two strings and print the result.
first_name = "Nikhil"
last_name = "Adi"
concatenate = first_name + " " + last_name
print(concatenate)

# Repeat a string three times and display the output.
name = "komal "
result = name * 3
print(result)

# 5. Python Keywords: Create a variable with a name that is a python keyword. what happens? Observation....
# raise = "funds"
# print(raise)
#Observation: It throws a syntax error says invalid syntax

# 6. Python Variables: Declare two variables, one storing an integer and the other a string. print their values
student_id = 1661
_student_name = "Nikhil"
print(student_id)
print(_student_name)

# 7. Type Conversions: Convert a float to an integer and print the result.
product_price = 499.97
product_price_1 = int(product_price)
print(product_price_1)
print(type(product_price_1))

# Convert an integer to a string and display the output.
age = 35
conv = str(age)
print(conv)
print(type(conv))

# 8. Take the user's age as input and print a message using the output.
age = input("Enter the age: ")
print(age)

#######  Exercise  ########
# 1. Print Statement.
print("*")
print("**")
print("***")
print("****")
print("*****")

# 2. Comments.
# This program calculates the average of three numbers

# Assign values to three variables
num1 = 10
num2 = 20
num3 = 30

#  Calculate the sum of the three numbers
total = num1 + num2 + num3

#  Calculate the average
average = total / 3

#  Print the results
print("Number 1:", num1)
print("Number 2:", num2)
print("Number 3:", num3)
print("Sum:", total)
print("Average:", average)


# 3. Data Structures & Data Types:
book = {
    "title": "Rich Dad Poor Dad",
    "author": "Robert Kiyosaki",
    "publication_year": 1997
}

print("Book Details:")
print(book)

print("\nTitle:", book["title"])
print("Author:", book["author"])
print("Publication Year:", book["publication_year"])

# 4. String Operations:
emp_1 = input("The String value is: ")
conv = float(emp_1)
print(conv) 

# 5. Concatenate Strings:
a = input("Enter the first_name: ")
b = input("Enter the last_name: ")
print(a + " " +b)

# 6. Type Conversions:
age = input("Enter your age: ")
conver= int(age)
print(conver + 5)
print(type(conver))

# 7. Simple Input & Output
_number_1 = int(input("enter the number: "))
_number_2 = int(input("enter the number: "))
print("Addition:",(_number_1 + _number_2))
print("Subtraction:",(_number_1 - _number_2))
print("Multiplication:",(_number_1 * _number_2))
print("Division:" ,(_number_1 / _number_2))