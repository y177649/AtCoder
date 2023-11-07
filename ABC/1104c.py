il=[]
sl=[]
for f1 in range(9):
    a=list(map(int,input().split()))
    if sum(a)==45:
        il.append(a)
        print('Yes')
        break
else:
    for f2 in range(9):
        for f3 in range(9):
            
