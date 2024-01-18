a,b=list(map(int,input().split()))

pri='No'

if a+1==b and a%3!=0:
    pri='Yes'

print(pri)