s=list(input())

eng=['a','e','i','o','u']
dust=[]
ans=[]

for in_s in s:
    if in_s in eng:
        dust.append(in_s)
    else:
        ans.append(in_s)

print(''.join(ans))