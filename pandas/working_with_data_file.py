# %%
import pandas as pd

# %%
# using encoding because file has cyrillic characters
df = pd.read_csv('data.txt', encoding='windows-1251')


# %%
df.head()

# %%
