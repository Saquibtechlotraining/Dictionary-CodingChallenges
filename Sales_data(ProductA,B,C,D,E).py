# You are given a dictionary sales_data containing sales information for a company's products.
# Each key-value pair in the dictionary represents a product's name and its corresponding sales in dollars for the year.

# sales_data = { 'Product A': 15000, 'Product B': 25000, 'Product C': 30000, 'Product D': 40000, 'Product E': 50000 }
# 1.Write a program to calculate the total sales for the company.
# 2.Write a program to calculate the average sales per product.
# 3.Write a program to find the best-selling product.

sales_data = {
    "Product A" : 15000,
    "Product B" : 25000,
    "Product C" : 30000,
    "Product D" : 40000,
    "Product E" : 50000
}
# 1.Total sales of company
total_sales = sum(sales_data.values())
print("Total Sales:", total_sales)

# 2.Average sales per product
total_length = len(sales_data)
print("Average Sales per product:", total_sales/ total_length)

# 3.Find best selling product
maximum_value = max(sales_data.values())   # 50000
for key, value in sales_data.items():     # Unpack of items
    if maximum_value == value:
        print(f"Best Selling Product- {key}: {value}")