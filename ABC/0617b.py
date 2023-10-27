a=list(map(int,input().split()))

x=[]

for f1 in range(64):
    x.append(a[f1]*2**f1)

print(sum(x))