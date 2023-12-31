# This is file 65
"""
a-b if x =2 <1 >3

a-b if + 3

"""
pri='null'
x,a,b=list(map(int,input().split()))

if a-b>1:
    pri='delicious'
else:
    if -x<(a-b):
        pri='safe'
    else:
        pri='dangerous'

print(pri)