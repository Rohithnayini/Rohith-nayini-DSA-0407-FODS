
import numpy as np

# Columns: Bedrooms, Square Footage, Sale Price
house_data = np.array([
    [3, 1200, 200000],
    [5, 2000, 350000],
    [4, 1500, 250000],
    [6, 2500, 450000],
    [5, 2200, 400000]
])

# Select houses with more than 4 bedrooms
selected_houses = house_data[house_data[:, 0] > 4]

# Extract sale prices (3rd column)
sale_prices = selected_houses[:, 2]

# Calculate average sale price
average_price = np.mean(sale_prices)

print("Average sale price:", average_price)
