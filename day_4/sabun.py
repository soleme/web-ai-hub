import random
import pandas as pd

sales = [random.randint(1,100) for i in range(16)]
sales.sort()
print(sales)

# 4등분
#n = (len(sales) // 4)
#print('count : ',n)
#print(f'{sales[n]},{sales[2*n]},{sales[3*n]}')

df = pd.DataFrame(sales, columns=['sales'])
print(df)

# 25%, 50%, 75%의 값을 구할수 있다. 사분위수
print(df['sales'].quantile([0, .25, .5, .75, 1]))

