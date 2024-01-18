a=int(input())
b=int(input())

if a==0 or b==0:
    print(b)
else:
    b_=0
    for f1 in range(100):
        if a>b_:
            b_+=b*(f1+1)

        else:
            print(b_-a)
            break