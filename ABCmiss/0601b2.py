n,m=map(int,input().split())

for i in range(n):
    a=list(input().split())
    
        if len(set(a))==1:
            print('Yes')
            print(i)