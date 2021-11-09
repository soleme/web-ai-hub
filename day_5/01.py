#최빈값 (데이터 빈도수)

fruit=['배','배','배','배','사과','사과','귤','귤','귤']
#print(set(fruit))

fruit_count = [(s, fruit.count(s)) for s in set(fruit)]
#print(fruit_count)

import pandas as pd

df = pd.DataFrame(fruit, columns=['fruit'])
print(df)

print("최빈값 : " ,df['fruit'].value_counts())

print("비율 : " ,df['fruit'].value_counts(normalize=True))