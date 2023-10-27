nhx=list(map(int,input().split()))
p=list(map(int,input().split()))

n=nhx[0]
h=nhx[1]
x=nhx[2]

list1=[]

for f1 in range(len(p)):
    if p[f1]>=(x-h):
        list1.append(p[f1])

list1.sort()

print(p.index(list1[0])+1)