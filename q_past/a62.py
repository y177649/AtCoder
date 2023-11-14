# This is file 62

x,y=list(map(int,input().split()))

res1=[]
if x in [1,3,5,7,8,10,12]:
    res1.append('g1')
elif x in [4,6,9,11]:
    res1.append('g2')
elif x==2:
    res1.append('g3')

res2=[]
if y in [1,3,5,7,8,10,12]:
    res2.append('g1')
elif y in [4,6,9,11]:
    res2.append('g2')
elif y==2:
    res2.append('g3')

if res1[0]==res2[0]:
    print('Yes')
else:
    print('No')