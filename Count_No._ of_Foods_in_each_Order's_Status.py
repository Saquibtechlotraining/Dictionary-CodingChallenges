# You have given a (list_of_food) dictionary in which the order's status is the key, and the list of food items
# is the values. You want to count the number of foods in each status?

list_of_food = {
    "pending" : ["pron", "sushi"],
    "shipped" : ["burger", "pizza"],
    "delivered" : ["chicken wings", "chicken tikka", "chicken roll"]
}
print(list_of_food)

for x, y in list_of_food.items():   # Unpack of items()
    print(f"Number of food in {x} is:", len(y))