from os import terminal_size
import matplotlib
from matplotlib.colors import Normalize
import seaborn as sns
import pandas as pd

df = sns.load_dataset('tips')
print(df.shape)
print(df.info())
df.head()

print(df.describe())

print(pd.DataFrame({'절대빈도' : df['day'].value_counts(),
                    '상대빈도' : df['day'].value_counts(normalize=True)}))

df['day'].value_counts().plot.pie(autopct='%0.1f%%')
