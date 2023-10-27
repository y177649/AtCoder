s=list(map(int,input()))

sx=s[1::2]

if sum(sx)==0:
    print('Yes')
else:
    print('No')