il=[]
cou=0
for f1 in range(9):
    a=list(map(int,input().split()))
    if sum(a)==45:
        cou+=1
    for f2 in range(9):