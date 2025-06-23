# This is file 92

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