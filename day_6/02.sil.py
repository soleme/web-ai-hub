#레모네이드 판매 데이터
#https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/lemonade.csv
# 보스턴 집값 데이터
#https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/boston.csv
# 아이리스 품종 데이터
#https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/iris.csv

import pandas as pd

path = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/boston.csv'
df = pd.read_csv(path)

print(df.groupby(['chas']).median())
print("")

path2 = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/iris.csv'
df = pd.read_csv(path2)
print(df.head())

print(df.groupby(['품종'])[['꽃잎길이','꽃잎폭']].describe())