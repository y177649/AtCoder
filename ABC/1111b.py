n=int(input())
d=list(map(int,input().split()))
cou=0
for f1 in range(len(d)):
    if d[f1]==f1+1:
        cou+=1
    elif d[f1]>=f1*11:
        cou+=f1+1

print(cou)