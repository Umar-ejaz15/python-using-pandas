# %%
import pandas as pd

s = pd.Series([1, 3, 5, 7])
print(s)
print(s[1])


# %%
data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
disc = pd.Series(data)
print(disc)
print(disc['a'])
print(disc['a':'b'])

# %%
s = pd.Series([1, 3, 5, 7], index=['a', 'b', 'c', 'd'])
print(s)

# %%
s = pd.Series(5, index=[1, 2, 3, 4])
print(s)
print(s[0:2])

# %%
