import FinanceDataReader as fdr
# 삼성전자 (005930)
df = fdr.DataReader('005930')
# print(df.shape)
print(df.tail)