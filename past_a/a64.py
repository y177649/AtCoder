# This is file 64

x=input().split()
result=''
for i in x:
    result+=i

int_x=int(result)

if int_x%4==0:
    print('YES')
else:
    print('NO')
