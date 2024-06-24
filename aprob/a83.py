# This is file 83


a,b,c,d=map(int,input().split())

if a+b == c+d :
    print('Balanced')

else:
    if a+b < c+d :
        print('Right')

    else:
        if a+b > c+d :
            print('Left')