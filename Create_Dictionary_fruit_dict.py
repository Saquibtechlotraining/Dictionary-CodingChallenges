# Create a dictionary called fruit_dict with the following key-value pairs:
# "apple" : 1, "banana" : 2, "orange" : 3. Also print fruit_dict.

fruit_dict = {}
for i in range(0, 3):
    key = input(f"Enter the {i+1} key:")  # 1-apple, 2- banana, 3- orange
    value = int(input(f"Enter the {i+1} value:"))  # 1, 2, 3
    fruit_dict[key] = value

print("fruit_dict:", fruit_dict)