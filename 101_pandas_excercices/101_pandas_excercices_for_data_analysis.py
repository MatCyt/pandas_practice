# 101 pandas excercices
# https://www.machinelearningplus.com/python/101-pandas-exercises-python/


# 1. How to import pandas and check the version?
import pandas as pd
import numpy as np
print(pd.__version__)

# 2. How to create a series from a list, numpy array and dict?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

series1 = pd.Series(mylist)
series2 = pd.Series(myarr)
series3 = pd.Series(mydict)

mydict
series3

# 3. How to convert the index of a series into a column of a dataframe?
series3['index'] = series3.index
series3

# 4. How to combine many series to form a dataframe?
df1 = pd.concat([series1, series2], axis = 1)
df1

df2 = pd.DataFrame({'col1': series1, 'col2': series2})
df2

# 5. How to assign name to the series’ index?
series1.name = 'alphabets'
series1

# 6. How to get the items of series A not present in series B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

ser1.loc[~ser1.isin(ser2), ]

# 7. How to get the items not common to both series A and series B?
ser_u = pd.Series(np.union1d(ser1, ser2))  # union
ser_i = pd.Series(np.intersect1d(ser1, ser2))  # intersect
ser_u[~ser_u.isin(ser_i)]

# 8. How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?

state = np.random.RandomState(100)
ser = pd.Series(state.normal(10, 5, 25))

np.percentile(ser, q = [0, 25, 50, 75, 100])

# 9. How to get frequency counts of unique items of a series?
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

ser.value_counts()

# 10. How to keep only top 2 most frequent values as it is and replace everything else as ‘Other’?
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

ser.value_counts()[:2]
ser[~ser.isin(ser.value_counts().index[:2])] = 'Other'

# 11. How to bin a numeric series to 10 groups of equal size?
ser = pd.Series(np.random.random(20))

pd.qcut(ser, q=[0, .10, .20, .3, .4, .5, .6, .7, .8, .9, 1])

# 14. How to extract items at given positions from a series
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]

ser.take(pos)

# 15. How to stack two series vertically and horizontally ?
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

# vertical
pd.concat([ser1, ser2], axis=0)

# horizontal
pd.concat([ser1, ser2], axis=1)

# 18. How to convert the first character of each element in a series to uppercase?
ser = pd.Series(['how', 'to', 'kick', 'ass?'])

ser.map(lambda x: x.title())

# 19. How to calculate the number of characters in each word in a series?
ser.map(len)
ser.map(lambda x: len(x))

# 21. How to convert a series of date-strings to a timeseries?
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05'])

pd.to_datetime(ser)

# 22. How to get the day of month, week number, day of year and day of week from a series of date strings?

ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
ser2 = pd.to_datetime(ser)

ser2.dt.day
ser2.dt.dayofweek
ser2.dt.dayofyear
ser2.dt.weekofyear

# 25. How to filter valid emails from a series?
emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'

emails.str.findall(pattern)

# 26. How to get the mean of a series grouped by another series?
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))

weights.groupby(fruit).mean()

# 29. How to replace missing spaces in a string with the least frequent character?
my_str = 'dbc deb abed gade'

ser = pd.Series(list('dbc deb abed gade'))
freq = ser.value_counts()
print(freq)
least_freq = freq.dropna().index[-1]
"".join(ser.replace(' ', least_freq))

# 30. How to create a TimeSeries starting ‘2000-01-01’ and 10 weekends (saturdays) after that having random numbers as values?

ser = pd.Series(np.random.randint(1, 10, 10), pd.date_range('2000-01-01', periods=10, freq = 'W-SAT'))
ser

# 36. How to import only specified columns from a csv file?

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv', usecols=['crim', 'medv'])

# 37. How to get the nrows, ncolumns, datatype, summary stats of each column of a dataframe?
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

#  number of rows and columns
print(df.shape)

# datatypes
print(df.dtypes)

# how many columns under each dtype
print(df.get_dtype_counts())
print(df.dtypes.value_counts())

# summary statistics
df_stats = df.describe()

# 38. How to extract the row and column number of a particular cell with given criterion?
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# Which manufacturer, model and type has the highest Price?
df.loc[df.Price == max(df.Price), ['Manufacturer', 'Model', 'Type']]

# 39. How to rename a specific columns in a dataframe?
# Rename the column Type as CarType in df
df = df.rename(columns = {'Type':'CarType'})
df.columns

# and replace the ‘.’ in column names with ‘_’.
df.columns = df.columns.map(lambda x: x.replace('.', '_'))

# 40. How to check if a dataframe has any missing values?
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

df.isnull().values.any()





# What is the row and column number of the cell with the highest Price value?