a=int(input())
b=int(input())
n=int(input())

if a<=b:
    max_=b
    min_=a
else:
    max_=a
    min_=b

for f1 in range(20000):
    if max_*(f1+1)%min_==0:
        min_co=max_*(f1+1)
        break
    
for f2 in range(20000):
    if min_co*(f2+1)>=n:
        print(min_co*(f2+1))
        break