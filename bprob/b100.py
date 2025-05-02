D,X = list(map(int,input().split()))

if X != 100:
    print((100**D)*X)
else:
    print((100**D)*(X+1))