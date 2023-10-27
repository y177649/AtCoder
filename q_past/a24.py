a,b,c,k=list(map(int,input().split()))
s,t=list(map(int,input().split()))

old=b*t
yng=a*s

if s+t<k:
    print(old+yng)
else:
    print(old+yng-(c*(s+t)))