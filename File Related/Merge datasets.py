import pandas as pd
import numpy as np
data1=pd.read_csv('inventory.csv')

data2=pd.read_csv('inventory2.csv')

merged_data = pd.merge(data1, data2, on='Product ID')

outer_join = pd.merge(data1, data2, on='Product ID', how='outer')
print(outer_join)
