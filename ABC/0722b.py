n,d=list(map(int,input().split()))

t=['o']*d
for f1 in range(n):
    s=input()
    for f2 in range(d):
        if s[f2]=='x':
            t[f2]='x'
'''
#参考コード
lng=0
ans=0
for f3 in t:
    if f3=='o':
        lng+=1
        ans=max(ans,lng)
    elif f3=='x':
        lng=0
print(ans)
'''

len_=0
ans=0
for f3 in t:
    if f3=='o':
        len_+=1
        if ans<=len_:
            ans=len_
    else:
        len_=0

print(ans)