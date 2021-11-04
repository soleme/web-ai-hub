import random
import pandas as pd

sales = [random.randint(1,100) for i in range(16)]
df = pd.DataFrame(sales, columns=['sales'])

# 기술적 통계
print(df.describe())
