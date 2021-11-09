import pandas as pd

url = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/boston.csv'

df = pd.read_csv(url)
# df.head()
df_selected = df[(df['chas'] == 1)]
print(df_selected)
print(df_selected.head())