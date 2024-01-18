x=input()

xj=list(map(str,x))

x1=set(x[0::3])
x2=set(x[1::3])
x3=set(x[2::3]) 

if len(set(x))==1 and len(xj)!=1 and len(xj)!=2:
    print('No')

elif len(x1)==1 and len(x2)==1 and len(x3)==1:
    print('Yes')

elif x=='o' or x=='x' or x=='xo' or x=='ox' or x=='xx':
    print('Yes')

else:
    print('No')

'''
test11 x or o
test12 x or o
test13 xx
test16 xxxx... or oooo...
'''