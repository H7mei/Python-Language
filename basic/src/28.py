# pandas
# high-level data analysis
# built by McKinsey & Company
import pandas as pd

# dataset in pyhton
# 2D array

# dataframe from dictionary
dict = {'country': ['Brazil', 'Russia', 'India', 'China', 'South Africa'],
        'year': [2000, 2001, 2002, 2003, 2004],
        'pop': [1.21, 1.28, 1.3, 1.4, 1.8]}

brics = pd.DataFrame(dict)
brics.index = ['BR', 'RU', 'IN', 'CH', 'SA']

print(brics)


# import data from csv
# csv: comma separated values

huricane = pd.read_csv('../path/csv/huricane.csv', index_col=0)

print(huricane)

# index and select data
# 1d array
# colums accessed by name
print(brics[['country', 'year']])
print(huricane['Average'])

# Discussion:
# 1. DataFrame is a 2D array
# 2. DataFrame is a collection of Series
# 3. Series is a 1D array
# 4. Series is a collection of values
# 5. Series is a collection of objects
# 6. Series is a collection of data
# 7. DataFrame is a collection of Series

# pandas: remarks
# loc and iloc: label-based and integer-based indexing
# kalo loc dari nama indexnya
# iloc dari indexnya

# row access
print(brics.loc[['IN', 'CH']])
print(brics.iloc[1])

# row column access
print(huricane.loc[['May', 'Aug'], 'Average'])
print(huricane.iloc[2, 3])
