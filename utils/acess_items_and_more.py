import numpy as np # not used at this point
import pandas as pd
import os # not used at this point
# Read excel file
draft = pd.read_csv('/home/labman/code/prj/input/Inventory_2024-10-01-12-00-00.csv')        

df = pd.DataFrame(draft,
                    columns=['column1', 'column2', 'column3', 'column4', 'column5'])

#print one cell with columnname on top and logical line
print(df.iloc[[0],[4]])
#print one called cell
#------------[row,column]
print(df.iloc[0,4])
# sum element + element
print(df.iloc[0,4] + df.iloc[4,4])
# sum of all elements from element to element in one column
print(df.iloc[0:6, 4].sum())

