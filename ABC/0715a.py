n,p,q=list(map(int,input().split()))

d=list(map(int,input().split()))

d.sort()

if p>q:
    big=p
    sma=q
else:
    big=q
    sma=p

if (d[0]+sma)<big:
    print(d[0]+sma)
else:
    print(big)