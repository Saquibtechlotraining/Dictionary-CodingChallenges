# Suppose you are working in a retail store and you want to keep track of sales by month.
# Write a program to create a dictionary sales_dict that stores the monthly sales data as follows:

# Month                                 Sales
# Jan                                   5000
# Feb                                   7000
# Mar                                   4500
# Apr                                   9000
# May                                   6000

# rite a program to:
# Print the sales in January.
# Print the total sales for the first quarter (Jan to Mar).
# Print the months in which sales were greater than 6000.
# Add the sales data for June (8000) to the dictionary.
# Remove the sales data for April from the dictionary.

sales_dict = {}
for i in range(0, 5):
    month = input(f"Enter the {i+1} month:").capitalize()
    sales = int(input(f"Enter {i+1} month sales:"))
    sales_dict[month] = sales
print(sales_dict)

# Print the Sales in January:
k = input("Enter the month of which we want a sales:").capitalize()
for key, val in sales_dict.items():  # Unpack of items
    if key == k:
        print(f"Sales in {k} is:", val)

# Print the total Sales for the first Quarter (January to March)
total_sales_quarter = sales_dict["Jan"] + sales_dict["Feb"] + sales_dict["Mar"]
print("Total Sales for the first quarter (January to March):", total_sales_quarter)

# Print the months in which sales were greater than 6000.
for month, sales in sales_dict.items():  # Unpack of items
    if sales > 6000:
        print(f"Months in which Sales were greater than 6000: {month}, and their sales is {sales}")

# Add the sales data for June (8000) to the dictionary.
sales_dict["June"] = 8000
print("New dictionary after adding sales data of June:", sales_dict)

# Remove the sales data for April from the dictionary
x = sales_dict.pop("Apr")
print("Dictionary after remove the sales data of April:", sales_dict)
