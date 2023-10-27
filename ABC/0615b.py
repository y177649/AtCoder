n=int(input())
y=n

cou2=0
cou3=0
for f1 in range(10**18):
    if n%2==0:
        n=n/2
        cou2+=1
    elif n%3==0:
        n=n/3
        cou3+=1
    else:
        break

if (2**cou2)*(3**cou3)==y:
    print('Yes')
else:
    print('No')