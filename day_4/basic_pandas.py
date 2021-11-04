import random
import pandas as pd

sales = [random.randint(1,10) for i in range(10)]

df = pd.DataFrame(sales, columns=['sales'])
print(df)