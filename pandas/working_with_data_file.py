
import pandas as pd

# using encoding because file has cyrillic characters
df = pd.read_csv('pandas/data.txt', encoding='windows-1251')


print(df)
