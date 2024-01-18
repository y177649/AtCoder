x=int(input())

def yen100(x):
    if x<100:
        print('No')
    elif x%100==0:
        print('Yes')
    else:
        print('No')

yen100(x)