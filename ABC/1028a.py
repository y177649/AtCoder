x,y=list(map(int,input().split()))

dif=y-x

print(dif)

#No  -3 <= dif
#No   2 <= dif 

if 2<dif or -3>dif:
    print('No')
else:
    print('Yes')