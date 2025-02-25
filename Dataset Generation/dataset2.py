import pandas as pd
import numpy as np

# Generate example sales data
num_values = 1465
sales_data = {
    'product_id': [f'Product_{i}' for i in range(1, num_values + 1)],
    'sales_quantity': np.random.randint(100, 500, size=num_values),
    'sales_date': pd.date_range(start='2023-01-01', periods=num_values, freq='M')  # Use 'M' instead of 'ME'
}

# Generate example promotional data
promotional_data = {
    'product_id': [f'Product_{i}' for i in range(1, num_values + 1)],
    'promotion_start_date': pd.date_range(start='2023-01-01', periods=num_values, freq='2M'),  # Use '2M' instead of '2ME'
    'promotion_end_date': pd.date_range(start='2023-01-01', periods=num_values, freq='3M'),  # Adjust end date to avoid out of bounds
    'promotion_type': np.random.choice(['Discount', 'BOGO', 'Flash Sale', 'Clearance', 'Seasonal'], size=num_values)
}

# Convert to DataFrames
sales_df = pd.DataFrame(sales_data)
promotional_df = pd.DataFrame(promotional_data)

# Save to CSV files for merging later
sales_df.to_csv('sales_data.csv', index=False)
promotional_df.to_csv('promotional_data.csv', index=False)
