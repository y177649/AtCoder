# This is file 67

a,b,=map(int,input().split())

if a%3==0:
    print('Possible')
else:
    if b%3==0:
        print('Possible')
    else:
        if (a+b)%3==0:
            print('Possible')
        else:
            print('Impossible')