# Create two dictionaries dict1 and dict2 with the following key-value pairs: "a" : 1, "b" : 2, "c" : 3 and "c" : 4, "d" : 5, "e" : 6 respectively.
# Write a program to merge dict2 into dict1.
# Write a program to create a new dictionary that contains only the key-value pairs that are common in both dict1 and dict2.
# Write a program to remove a key-value pair from dict1.

# Dictionary(dict1)
dict1 = {}
for i in range(0, 3):
    key1 = input(f"Enter the {i+1} key of dict1:")
    if not len(key1) == 1:                   # if length of any key is more than 1, the program break
        print("Every key must of 1 character")
        break
    value1 = int(input(f"Enter the {i+1} value in dict1:"))
    dict1[key1] = value1
print("dict1:", dict1)

# Dictionary(dict2)
dict2 = {}
for j in range(0, 3):
    key2 = input(f"Enter the {j+1} key of dict2:")
    if not len(key2) == 1:                   # if length of any key is more than 1, the program break
        print("Every key must of 1 character")
        break
    value2 = int(input(f"Enter the {j+1} value in dict2 :"))
    dict2[key2] = value2
print("dict2:", dict2)

# New dict1 dictionary after merging:-

dict1.update(dict2)         # To merge two dictionary we use update method
print("Merge dict2 into dict1:", dict1)

# Create new dictionary that contains only key value pairs that are common in both dict1 & dict2
common_dict = {k: dict1[k] for k in dict1 if k in dict2 and dict1[k] == dict2[k]}
print("Common key-value pair of dict1 and dict2:", common_dict)

# To remove a key-value pair from dict1
remove_key = input("Enter the key to be removed from dict1:")
dict1.pop(remove_key)
print(f"dict1 after removed {remove_key} key and its value:", dict1)

