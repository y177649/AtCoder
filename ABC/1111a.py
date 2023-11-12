n,x=map(int,input().split())
s=list(map(int,input().split()))
s.sort()
cou=0
for f1 in range(n):
    if x>=s[f1]:
        cou+=s[f1]
    else:
        break

print(cou)