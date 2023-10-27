n=int(input())
a=list(map(int,input().split()))

a.sort()

dif1=a[1]-a[0]
dif2=a[2]-a[1]

dif=min([dif1,dif2])

#print(dif)
dust=[]

for f1 in range(n-1):
    if a[f1]+dif==a[f1+1]:
        dust.append('d')
    else:
        print(a[f1]+dif)
        break