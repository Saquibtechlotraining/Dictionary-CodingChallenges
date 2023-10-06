# Ascending and Descending order of dictionary according to sorted values.

laptop = {
    "macbook" : 100000,
    "lenovo" : 61000,
    "asus" : 58000,
    "razer" : 150000,
    "hp" : 50000
}
print("Ascending Order:", dict(sorted(laptop.items(), key = lambda x: x[1])))
print("Descending Order:",dict(sorted(laptop.items(), key = lambda x: x[1], reverse = True)))

# Find Maximum value:-
dict_1 = {
    "macbook" : 100000,
    "lenovo" : 61000,
    "asus" : 58000,
    "razer" : 150000,
    "hp" : 50000
}
max_key = max(dict_1, key = dict_1.get)  # Return key of maximum value
max_value = dict_1[max_key]              # Return maximum value
print(f"The maximum value is {max_value} and its key is {max_key}")

# Find Minimum value:-
dict_1 = {
    "macbook" : 100000,
    "lenovo" : 61000,
    "asus" : 58000,
    "razer" : 150000,
    "hp" : 50000
}
# Method-1
min_key = min(dict_1, key = dict_1.get)     # Return key of maximum value
min_value = dict_1[min_key]                 # Return maximum value
print(f"The minimum value is {min_value} and its key is {min_key}")

# Method-2 (Using for Loop) to find Minimum value:-
min_value = min(dict_1.values())

for key, value in dict_1.items():
    if min_value == value:
        print(f"The minimum value is {value} and its key is {key}")