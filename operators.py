# AREA OF RECTANGLE 
_length = int(input("Enter length of Rectangle :"))
_width = int(input("Enter width of Rectangle :"))

area = _length * _width
print(area)

# INCREMENT AND DECREMENT 
Book_price = 499
print("original price :", Book_price)
Increase_price = Book_price+51
print("After increment :", Increase_price)
Book_price -= 49
print("After Decrement :", Book_price)

# Celsius to Fahrenheit.
celsius = float(input("Enter Temparature :"))
F = (celsius * 9/5) + 32 
print("Temperature in Fahrenheit:", F)

# SIMPLE INTEREST 
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest is:", simple_interest)


# STRING CONCATENATE 
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = string1+" "+string2

print("Concatenated string:", result)

# KILOMETERS TO MILES 
kilometers = float(input("Enter distance in kilometers: "))

miles = kilometers * 0.621371

print("Distance in miles:", miles)


# <----------###### EXCERCISE ######--------->

# F-String
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"This is  {name}! iam {age} years old.")

#check numbers in list 

My_list = [1,2,3,4,5,6,7,8,9,10]

print("Is 5 in the list?", 5 in My_list)
print("Is 15 in the list?", 15 in My_list)
