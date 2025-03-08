# %%
import pandas as pd
df = pd.read_csv('Psl_Complete_Dataset(2016-2024).csv')

print(df.isnull().sum())

# %%

# %%

# Fill missing values with 0
df_filled_0 = df.fillna(0)

# Compute mean only for numeric columns
print(df_filled_0.mean(numeric_only=True) * 100)

# Fill missing values with column mean (numeric columns only)
df_filled_mean = df.fillna(df.mean(numeric_only=True))
print(df_filled_mean)

# %%
df_dropna_rows = df.dropna()
print(df_dropna_rows)

df_dropna_columns = df.dropna(axis=1)
print(df_dropna_columns)

df_dropna_all = df.dropna(how='all')
print(df_dropna_all)

df_dropna_thresh = df.dropna(thresh=3)
print(df_dropna_thresh)

# %%


# %%
