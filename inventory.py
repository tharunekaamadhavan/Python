import pandas as pd
import numpy as np
data1=pd.read_csv('inventory.csv')
print(data1)
data2=pd.read_csv('inventory2.csv')
print(data2)
merged_data = pd.merge(data1, data2, on='Product ID')
print(merged_data)
