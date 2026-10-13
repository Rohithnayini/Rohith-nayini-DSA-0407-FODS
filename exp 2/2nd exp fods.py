
import numpy as np

# 3x3 matrix representing sales prices of 3 products
sales_data = np.array([
    [100, 150, 200],
    [250, 300, 350],
    [120, 180, 240]
])

# Calculate average price of all products
average_price = np.mean(sales_data)

print("Average price of all products:", average_price)
