import pandas as pd
import csv

df = pd.read_csv("dwarf_stars.csv")
print(df.shape)

missing_values = ['n/a', 'na', '--']
data =pd.read_csv('dwarf_stars.csv', na_values = missing_values)
data.head()

df.to_csv("main.csv")