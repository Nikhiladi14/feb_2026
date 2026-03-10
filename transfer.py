numbers = [25, 30, 20, 40, 15, 25]

total = 0

for num in numbers:
    total += num
    if total > 100:
        print("Sum exceeded 100")
        break

print("Sum:", total)

# Skipping Even numbers

for i in range(1, 601):
    if i % 2 == 0:
        continue
    print(i)

#Print Even or pass

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    pass


# Write a Python script that iterates through a list of words. If the word is "break," exit the loop using the break statement. If the word is "skip," skip the rest of the code for the current iteration using the continue statement. For any other word, print the word.
words = ["Hello", "skip", "world", "break", "python", "code"]

for word in words:
    if word == "break":
        break
    elif word == "skip":
        continue
    else:
        print(word)