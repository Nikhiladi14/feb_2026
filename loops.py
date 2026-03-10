
#  sum of the squares of numbers from 1 to 5

sum = 0
for i in range(0,6):
    sum += i**2

print(sum)


# while loop to print a countdown from 5 to 1.

total = 5

while total > 0:
    print(total)
    total -= 1

# multiplication table for a user-specified number using a nested for loop

num = int(input("Enter a number: "))

for i in range(1, 2):
    for j in range(1, 11):
        print(f"{num} x {j} = {num * j}")


# Python program that uses a "for" loop to find the sum of all even numbers between 0 and 10 
total = 0

for i in range(0, 11):
    if i % 2 == 0:
        total += i

print("Sum of even numbers from 0 to 10 is:", total)


# sum of all numbers from 1 to a given number
num = int(input("Enter a number :"))
total = 0 
for i in range(0,num + 1):
    total += i
print(total)

#Display a list numbers using Loop 
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
for num in numbers:
    print(num)


# Display numbers from -10 to -1 using for loop

for i in range(-10,-1):
    print(i)


# cube

num_1 = int(input("Enter a number: "))
sum = 0

for i in range (0,num_1):
    sum = i*i*i
    print(sum)