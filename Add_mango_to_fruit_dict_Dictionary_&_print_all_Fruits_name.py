# Write a program to add a fruit mango in the fruit_dict and print all the fruit names.

fruit_dict = {
    "apple" : 1,
    "banana" : 2,
    "orange" : 3
}
fruit_dict["mango"] = 4
for key in fruit_dict.keys():
    print(key)
