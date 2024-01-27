s=input()

dic_s={}
for f1 in range(len(s)):
    sf=s[f1]
    if s[f1] in dic_s:
        dic_s[sf]+=1
    else:
        dic_s[sf]=1
    
ma,mz=0,""
sort_dic=sorted(dic_s.items())#,reverse=True)

dic_s.clear()
dic_s.update(sort_dic)

#print(dic_s)

for f2 in dic_s.keys():
    if dic_s[f2]>ma:
        mz,ma=f2,dic_s[f2]
print(mz)