n=int(input())

import pandas as pd

ans=[]

for f1 in range(n):
    s=input()
    ans.append([s.count('o'),f1+1])

df=pd.DataFrame(ans)
df_s=df.sort_values(0,ascending=False)
l_df=df_s.values.tolist()

ans_=[]

for f2 in range(n):
    ans_.append(l_df[f2][1])

print(ans_)