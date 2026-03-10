#mode 'r'

file = open("sample.txt", "r")
data = file.read()
print(data)
file.close()

#mode 'w'
file = open("sample.txt", "w")
file.write("Hello Nikhil\n")
file.write("Python File Handling")
file.close()

#append 'a'

file = open("sample.txt", "a")
file.write("\nThis is appended text.")
file.close()

#Mode 'x'

file = open("newfile.txt", "x")
file.write("New file created.")
file.close()

#mode 'r+'
file = open("sample.txt", "r+")
print(file.read())
file.write("\nAdded using r+")
file.close()

#mode 'w+'
file = open("sample.txt", "w+")
file.write("New content")
file.seek(0)  
print(file.read())
file.close()

#mode 'a+'
file = open("sample.txt", "a+")
file.write("\nAppending with a+")
file.seek(0)
print(file.read())
file.close()