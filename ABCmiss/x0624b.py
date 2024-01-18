import itertools

n=int(input())

y=0
x=[]

for i in range(n):
    s=input()
    x.append(s)
  
for j in itertools.combinations(x, 2):
    if (z:=(''.join(j)))==z[::-1]:
        y+=1
        print(j)

if y>0:
    print('Yes')
else:
    print('No')