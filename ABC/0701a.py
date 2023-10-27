pri='No'

x=list(map(int,input().split()))

y=sorted(x)

if x==y and min(x)>=100 and max(x)<=675 and sum(x)%25==0:
    pri='Yes'

print(pri)
