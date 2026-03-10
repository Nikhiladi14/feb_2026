# reverse the elements

my_list = [10, 20, 30, 40, 50, 11]
my_list.reverse()
print(my_list)

#print common elements 

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
 
Empty_list = []

for i in list1:
    if i in list2:
        Empty_list.append(i)

print("common elements:", Empty_list)

# Unique elements 
original_list = [1, 2, 2, 3, 4, 4, 5]   
Unique_list = []

for i in original_list:
    if i not in Unique_list:
        Unique_list.append(i)

print("Unique list:",Unique_list )


# Remove duplicate elements 

duplicated_list = [1, 2, 2, 3, 4, 4, 5] 
Empty_list = []

for i in duplicated_list:
    if i not in Empty_list:
        Empty_list.append(i)

print("List without duplicates:", Empty_list)

# List Concatenation

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print("Concatenated List:", result)

# List Repetition

my_list = [1, 2, 3]

result = my_list * 3

print("Repeated List:", result)

# Remove Elements at Even Indices

my_list = [10, 20, 30, 40, 50, 60]

result = [my_list[i] for i in range(len(my_list)) if i % 2 != 0]

print("List after removing even index elements:", result)


# Insert 10, 11, 12 at Beginning

my_list = [1, 2, 3, 4]

my_list = [10, 11, 12] + my_list

print("Updated List:", my_list)