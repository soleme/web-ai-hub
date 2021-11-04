import random

sales = [random.randint(1,10) for i in range(10)]
print(sales)

mean = sum(sales) / len(sales)
print(mean)
