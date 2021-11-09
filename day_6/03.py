import pandas as pd
df1 = pd.DataFrame([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
df2 = pd.DataFrame([[1,2,3,5],[4,5,6,7],[7,8,9,10]])

print(df1.shape, df2.shape)

df_concat = pd.concat([df1,df2], axis = 1)
print(df_concat.shape)

print("")

df_concat.columns = [0,1,2,3,4,5,6,7]
print(df_concat)

print("")

df_concat = pd.concat([df1, df2], axis = 0)
print(df_concat.shape)
print(df_concat)

print("")

# 인덱스 갱신
df_concat = df_concat.reset_index(drop=True)
print(df_concat)
