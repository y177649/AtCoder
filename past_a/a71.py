# This is file 71

x,a,b=list(map(int,input().split()))

saa=abs(x-a)
sab=abs(x-b)

if saa<sab:
    print('B')
else:
    print('A')