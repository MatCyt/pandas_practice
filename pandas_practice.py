# PANDAS TEST
import pandas as pd

# Load dataset
df = pd.read_csv('IMDB-Movie-Data.csv')

# Show top and last rows
df.head(2)
df.tail(2)

# DF - basic information
df.info()
df.shape

## Understand variables
df.describe()

# Describe one column
df['Genre'].describe()

# Frequency count
df.Genre.value_counts()

## Duplicates
df_new = df.drop_duplicates()
# or
df.drop_duplicates(inplace = True)


## Column cleanup
df.columns

# Columns rename
df.rename(columns={
        'Runtime (Minutes)': 'Runtime', 
        'Revenue (Millions)': 'Revenue_millions'
    }, inplace=True)

df.columns

# lowercase columns
df.columns = [col.lower() for col in df]
df.columns


## Missing data

# see missing data
df.isnull()

# count missing by column
df.isnull().sum()

# remove null values
df.dropna() #inplace = True

# drop column with missing values
df.dropna(axis = 1)

# impute missing values - revenue millions
df.revenue_millions.fillna(df.revenue_millions.mean(), inplace = True)
df.isnull().sum()

df.columns


## Correlations
df.corr()


## Slicing and indexing

# BY COLUMN
df['rank'] # regular - extract as SERIES
df.rank # Pandas

df[['rank']] # extract as data frame

# extract two columns as data frame
df[['rank', 'genre']]

# BY ROW
# .loc by name
df.loc["Prometheus"]

# iloc for row number
df.iloc[1]

# for 4 rows
df.iloc[1:4]

# Combine that - select multiple rows and columns
# by number
df.iloc[1:3, 2:5]

# by name
df.loc[1:3, ['genre', 'description']]


# Boolean
# columns greater than
dummydf[dummydf.A > 0]


## Conditional Selection

# Directed by Ridley Scott
df['director'] == 'Ridley Scott' # True False

df[df['director'] == "Ridley Scott"] # Select films

# Films with rating above 8.6
df[df['rating'] >= 8.6].head(3)

# Let's filter the the DataFrame to show only movies by Christopher Nolan OR Ridley Scott:
df[(df['director'] == 'Christopher Nolan') | (df['director'] == 'Ridley Scott')].head()


# Applying functions

def rating_function(x):
    if x >= 0.8:
        return 'good'
    else:
        return 'bad'

df["rating_category"] = df["rating"].apply(rating_function)

df.head(5)




