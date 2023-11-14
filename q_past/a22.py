n,s,t=list(map(int,input().split()))
w=int(input())

a_=0
res=0
s_=s-w
t_=t-w

if  w>=s and w<=t:
        res+=1

for f1 in range(n-1):
    a=int(input())
    a_+=a

    if a_>=s_ and a_<=t_:
        res+=1

print(res)