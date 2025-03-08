# %%
import pandas as pd

data = {
    'name': ['umair', 'ali', 'ahmed'],
    'age': [20, 21, 22],
    'city': ['lahore', 'karachi', 'islamabad'],
    'country': ['pakistan', 'pakistan', 'pakistan']
}

df = pd.DataFrame(data)

df['profession'] = ['dev', 'designer', 'analyst']

print(df)


# %%
df.drop(columns=['city'], inplace=True)

print(df)
# %%
df.rename(columns={'name': 'full_name'}, inplace=True)
print(df)
# %%
