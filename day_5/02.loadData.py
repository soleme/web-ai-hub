#레모네이드 판매 데이터
#https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/lemonade.csv
# 보스턴 집값 데이터
#https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/boston.csv
# 아이리스 품종 데이터
#https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/iris.csv

import pandas as pd
path = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/lemonade.csv'
df = pd.read_csv(path)
df_sorted = df.sort_values(by=['판매량'], ascending=False)
# print(df_sorted.head())
# print(df_sorted.iloc[0])
# print(df_sorted.loc[0])
#print(df['온도'] > 23)
#print(df[(df['온도']>23)])
#print(df[(df['온도']>23) | (df['판매량'] == 40)])

d = {'col1':['1','2','3','4'],
     'col2':['Gold','Bronze','Gold','Silver']}
df1 = pd.DataFrame(d)
# print(df1)

print(df1.col2.str.contains('o'))
print(df1[df1.col2.str.contains('o')])

# path = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/iris.csv'
# df = pd.read_csv(path)

# # 행과 열의 개수를 파악
# print(df.shape)
# # 표의 대략적인 정보를 파악
# print(df.info())

# # 기본5개 보여준다.
# print(df.head(2))
# print(df.tail(2))
# print(df.columns)