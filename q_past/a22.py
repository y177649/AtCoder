n,s,t=list(map(int,input().split()))
w=int(input())

a_=0
ans=0
s_=s-w
t_=t-w

if  w>=s and w<=t:
        ans+=1

for f1 in range(n-1):
    a=int(input())
    a_+=a

    if a_>=s_ and a_<=t_:
        ans+=1

print(ans)