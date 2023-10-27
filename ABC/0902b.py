"""
n=int(input())

ab=[]
cd=[]

for f1 in range(n):
    a,b,c,d=map(int,input().split())
    ab+=[a,b]
    cd+=[c,d]

x_max_ab=max(ab)
y_max_bc=max(cd)

xy=[]
for f2 in range(y_max_bc):
    #print('#'*x_max_ab)
    xy.append(list('#'*x_max_ab))

#print(xy)

xy[4][1]='.'

print(xy)

"""
x=list(map(int,input().split()))

x[0]=x[0]+1
x[2]=x[2]+1

#print(x)

a=x[0]
b=x[1]-(x[0]-1)
cd=[x[2],x[3]]

print(a)
print(b)
print(cd)

ylist=[f4+b-1 for f4 in range(a)]

print(ylist)