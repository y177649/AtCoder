# This is file 92

"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

result_ab = 0
result_cd = 0

if a<b :
    result_ab = a
else:
    result_ab = b

if c<d :
    result_cd = c
else:
    result_cd = d

print(result_ab + result_cd)
"""
"""
ls = []
x=0

result_ab = 0
result_cd = 0

for i in range(4):
    x = int(input())
    ls.append(x)

if ls[0] < ls[1]:
    result_ab = ls[0]
else:
    result_ab = ls[1]
if ls[2] < ls[3]:
    result_cd = ls[2]
else:
    result_cd = ls [3]

print(result_ab + result_cd)
"""
"""
ls = []
x=0

for i in range(4):
    x = int(input())
    ls.append(x)

print(min(ls[0],ls[1]) + min(ls[2],ls[3]))
"""