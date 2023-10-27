n=input()
p=list(map(int,input().split()))

if len(p)==1:
    print(0)
    exit()

p1=p[0]
p2=max(p[1:])

if p1>p2:
    print(0)

else:
    print(p2-p1+1)