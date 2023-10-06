# Create a dictionary my_dict with three key-value pairs: "name" : "John", "age" : 30, "city" : "New York".
# Write a program to check if the key "name" is in my_dict.
# Write a program to check if the value "Chicago" is in my_dict.
# Write a program to get the length of my_dict.
# Write a program to clear all the elements in my_dict

my_dict = {}
for i in range(0, 3):
    key = input(f"Enter the {i+1} key:")
    value = input(f"Enter the {i+1} value:")
    my_dict[key] = value
print("my_dict:", my_dict)


key_name = input("Enter the key which we want to check in my_dict:")
if key_name in my_dict.keys():
    print(f"Yes, {key_name} key is present in my_dict")
else:
    print(f"This {key_name}key not present in my_dict")

if "Chicago" in my_dict.values():
    print("Yes, Chicago value present in my_dict")
else:
    print("No, Chicago value not present in my_dict")

print("Length of my_dict:", len(my_dict))   # Length of dictionary (my_dict)
print(my_dict.clear())

