# %% [markdown]
# # Pandas cntd 🐼

# %%
import pandas as pd

# %%
data = data = {"a":[1,2,3,4],
       "b":[4,5,6,7],
       "c":["Queso" , "Costeño","con","Bollo"]}

# %%
data

# %%
df = pd.DataFrame(data)

# %%
df

# %%
df.set_index('c', inplace=True)

# %%
df

# %%
df.reset_index()

# %%
data = data = {"a":[1,2,3,4],
       "b":[4,5,6,7],
       "c":["Queso" , "Costeño","con","Bollo"]}
df1 = pd.DataFrame(data,index = ['a','b','c','d'])

# %%
df1

# %%
df1.reindex(['b', 'c', 'a', 'd'])

# %%
# We can iterate over rows using iterrows
for i in df1.iterrows():
    print(i)


# %%
# Similarly we can use iter items

for i in df1.iteritems():
    print(i)

# %%
df1

# %%
# adding rows
def test(x):
    return x.sum()
df1.apply(test,axis=0)

# %%
df2 = df1[['a', 'b', ]]

# %%
df2

# %%
df2.applymap(lambda x: x**2)

# %%
# Sorting columns in alphabetical order
df1


# %%
df1.sort_values('c')

# %%
df1.sort_index(ascending=False)

# %%
# Working with text data

# %%
pd.set_option('display.max_colwidth', 500)
df3 = pd.DataFrame({'desc': ['New and Returning Students: Receive 50% off your first month on all Monthly Plans at New Masters Academy! Cancel at any time. Enroll with special promo code: OPENHOUSE23', 'I can recommend this course', 'Maybe try to include more variety in the sculpture curriculum']})

# %%
df3

# %%
df3['char_length_data'] = df3['desc'].apply(len)

# %%
df3

# %%
# Say we want to keep the wordcount, we can just use '.split()'
df3['word_count'] = df3['desc'].apply(lambda x: len(x.split()) )

# %%
df3

# %%
# Math ops
df1

# %%
df1['a'].mean()

# %%
df1['a'].median()

# %%
df1['a'].mode()

# %%
df1['a'].std()

# %%
df1['a'].max()

# %%
df1['a'].sum()

# %%
df1['a'].var()

# %%
# Windows function

# %%
df4 = pd.DataFrame({'a':[1,2,3,4,5,6,7,8,9]})

# %%
df4

# %%
df4.rolling(window=1).mean()

# %%
df4.rolling(window=2).mean()

# %%
df4.rolling(window=3).mean()

# %%
# Cumulative Sum
df4.cumsum()

# %%
# Date Functionality

# %%
data = pd.date_range(start= '2022-03-06', end ='2025-06-06')

# %%
data

# %%
# Converting it into df
df_date = pd.DataFrame({'date': data})

# %%
df_date

# %%
df_date.dtypes

# %%
df7 = pd.DataFrame({'date':['2022-03-09','2025-06-02' , '2025-06-04']})

# %%
df7

# %%
df7.dtypes # we passed datetime to obj to be able to perform more oprtions w it

# %%
pd.to_datetime(df7['date'])

# %%
df7['update_date'] = pd.to_datetime(df7['date'])

# %%
df7

# %%
df7.dtypes

# %%
# Extracting date 
df7['year'] = df7['update_date'].dt.year

# %%
df7

# %%
df7['day'] = df7['update_date'].dt.day

# %%
df7

# %%
# Time delta
time = pd.Timedelta(days =1, hours=5, minutes = 5)

# %%
dt = pd.to_datetime('2025-06-02')

# %%
dt + time

# %%
## Categorical Data

data = ['Karol', 'Miko', 'Quevedo', 'Peso', 'Bzrp']

# %%
cat = pd.Categorical(data)

# %%
cat.value_counts()

# %%
# Viz w pandas :)

d = pd.Series([1,2,3,4,5,6,7,8,9])

# %%
d.plot()

# %%


# %%



