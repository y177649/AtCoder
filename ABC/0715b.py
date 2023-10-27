n,m=list(map(int,input().split()))

p=[]
c=[]
f=[]

for f1 in range(n):
    pcf=list(map(int,input().split()))
    p.append(pcf[0])
    c.append(pcf[1])
    f.append(pcf[2:])

print(p)
print(c)
print(f)    