#1.try and except example
try:
    num_1=int(input("Enter first number:"))
    num_2=int(input("Enter second number:"))
    result=num_1/num_2
    print("Result:",result)
except ZeroDivisionError:
    print("Error:cannot divide by zero")

#2.else block
try:
    num = int(input("Enter a number: "))
    result = 7 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Result is:", result)

#3.finally block
try:
    num_1=int(input("Enter first number:"))
    num_2=int(input("Enter second number:"))
    result=num_1/num_2
    print("Result:",result)
except ZeroDivisionError:
    print("Error:cannot divide by zero")
finally:
    print("Executed successfully!")

# 4.Value error
try:
    num = int("abc")   
except ValueError:
    print("ValueError occurred, Cannot convert string to integer.")

# 5.Type error:
try:
    result = "10" + 7
except TypeError:
    print("TypeError occurred ,wrong data types.")

# 6.filenotfounderror
try:
    file = open("sample.txt", "r")
except FileNotFoundError:
    print("FileNotFoundError, File not found.")

#7.zerodivisionerror
try:
    a = 7
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("ZeroDivisionError, Cannot divide by zero.")

#8.Indexerror
try:
    list1 = [1, 2, 3]
    print(list1[5])
except IndexError:
    print("IndexError! List index out of range.")

#9.keyerror
try:
    dict = {"name": "Nikhil"}
    print(dict["age"])
except KeyError:
    print("KeyError! Key not found in dictionary.")

#10.object error
try:
    x = 10
    x.append(5)  
except AttributeError:
    print("AttributeError! Attribute not found.")

#11.overflow
import math
try:
    print(math.exp(10))
except OverflowError:
    print("OverflowError, Number too large.")

#12.IOerror
try:
    file = open("demo.txt", "r")
    file.write("Hello") 
except IOError:
    print("IOError! Cannot perform I/O operation.")

#13.RunTimeerror
try:
    raise RuntimeError("Something went wrong!")
except RuntimeError:
    print("RuntimeError occurred!")

#14.Exception ---> Base class of all exceptions
try:
    num = int("abc")
except Exception as e:
    print("Exception found")
    print("Error message:", e)


