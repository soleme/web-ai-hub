# 표준편차
# 평균으로 부터의 평균거리, 편차들의 평균
import random
import pandas as pd
import math

sales = [random.randint(1,10) for i in range(10)]

df = pd.DataFrame(sales, columns=['sales'])
print(df)

mean = sum(sales) / len(sales)
print('평균 :',mean)

deviations = [s - mean for s in sales]
print(deviations)

#분산
std = sum([d ** 2 for d in deviations]) / len(deviations)
#표준편차
print(math.sqrt(std))

#판다스에서 표준편차
print(df['sales'].std())

sales.sort()
print(sales)

# // - 몫을 구하는 연산자
n = len(sales) // 2 
print('몫 :',n)

if len(sales) % 2 == 0:
    print(sum(sales[n-1:n+1])  /2)
else:
    print(sales[n])

medium = df['sales'].median()
print('중앙값 : ',medium)