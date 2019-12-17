import numpy as np
import pandas as pd 

# Dataset creation - from dictionary

df = pd.read_csv('IMDB-Movie-Data.csv')


df.head(4)

df[['Director', 'Title']]

df.loc[1]

df.iloc[1]

df.shape

zoo = pd.read_csv('zoo.csv')

zoo
sum(zoo.water_need)

zoo.count()

zoo.animal.count()

zoo.water_need.min()
zoo.water_need.max()

zoo.sort_values(['water_need'], ascending = True)

zoo.groupby('animal').sum()
zoo.groupby('animal').sum()[['water_need']]
zoo.groupby('animal').sum().water_need


df.groupby('source').count()

zoo_eats = pd.read_csv('zoo_eats.csv', delimiter = ';')

zoo.merge(zoo_eats, how = 'outer').fillna('unknown')

zoo.sort_values(['water_need']).reset_index()