# Write a program to create a dictionary which contains the fruit name and their prices(float).
# Take fruit name and prices from user. Create for 5 fruits.

dict_1 = {}
for i in range(0, 5):
    key = input(f"Enter the {i+1} fruit name:").capitalize()
    value = float(input(f"Enter the {i+1} fruit price:"))
    dict_1[key] = value
print("5 Fruits:",  dict_1)

