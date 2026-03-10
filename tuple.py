#  creates a tuple containing three elements: your name, your age, and your favorite color.

my_info =  ("Nikhil", 21 , "Blue")
print("My information :")
print(my_info)

'''Write a program that creates a tuple containing the
days of the week. Then, print the third element of the tuple'''

week_tuple = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("The third day of the week is:",week_tuple[2])

"""Write a program that creates two tuples, one
containing odd numbers from 1 to 5 and another containing even numbers
from 2 to 6. Concatenate these two tuples and print the result"""

odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)
result = odd_numbers + even_numbers
print("concatenate:", result)

"""Write a program that defines a tuple containing the
dimensions of a rectangle (length and width). Then, unpack this tuple into
two variables and calculate the area of the rectangle.
"""

dimensions = (20,5)
length,width = dimensions

area = length * width 

print("length:", length)
print("width:", width)
print("area of rectangle:",area)

#Write a program that checks if a given element exists in a tuple.
numbers = (10, 20, 30, 40, 50)
element = int(input("Enter the Number :"))

if element in numbers:
        
        print("Given element exists in tuple")
else:
      print("Given element does not exists")


"""Write a Python program to generate a bill for a supermarket purchase. The
program should store the items and their prices in a list of tuples. It should
then iterate over this list to print out each item along with its price. Finally,
calculate and print the total cost of all the items
"""
items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]

print("Item      Price")
print("-" * 20)

total = 0

for item, price in items:
    print(f"{item:<10} {price:.2f}")
    total += price

print("-" * 20)
print(f"{'Total':<10} {total:.2f}")