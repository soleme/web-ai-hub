#레모네이드 판매 데이터
#https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/lemonade.csv
# 보스턴 집값 데이터
#https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/boston.csv
# 아이리스 품종 데이터
#https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/iris.csv

import pandas as pd

path = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/iris.csv'
df = pd.read_csv(path)
print(df.head())

# print("sum()")
# print(df[['꽃잎길이','꽃잎폭']].sum())

# print("mean()")
# print(df[['꽃잎길이','꽃잎폭']].mean())

# print("std()")
# print(df[['꽃잎길이','꽃잎폭']].std())

# print("median()")
# print(df[['꽃잎길이','꽃잎폭']].median())

# print("min()")
# print(df[['꽃잎길이','꽃잎폭']].min())

# print("max()")
# print(df[['꽃잎길이','꽃잎폭']].max())

# print(df.groupby(['품종'])[['꽃잎길이','꽃잎폭']].sum())
# print(df.groupby(['품종'])[['꽃잎길이','꽃잎폭']].mean())
# print(df.groupby(['품종'])[['꽃잎길이','꽃잎폭']].std())

print(df.groupby(['chas'])[['꽃잎길이','꽃잎폭']].sum())

