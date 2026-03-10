#Print the characters at even indices
sentence = "Python is amazing"
result = sentence[::2]
print(result)

# #Replace all spaces in the string with underscores ( _ )
# and print the modified string.
s = "Python is fun and powerful"

modified = s.replace(" ", "_")

print(modified)


# You are given a string s . Check if the string contains only digits

s = "12345"
if s.isdigit():
    print("String contain only digits")
else:
    print("String does not contain only digits")



# You are given a string s . Print the string in reverse order

s = "Python is amazing" 
reverse = s[::-1]
print(reverse)

# You are given a string s . Capitalize the first letter of each word in the string
# and print the modified string.
s = "python programming is fun"
 
result = s.title()
print(result)

