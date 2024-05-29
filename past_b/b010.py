
#input_________

II=lambda:int(input())
MIS=lambda:map(int,input().split())
LMI=lambda:list(map(int,input()))
LMIS=lambda:list(map(int,input().split()))
I=lambda:input()
L=lambda:list(input())
S=lambda:input().split()
#FI=[input() for _ in range(n)]

#code___________

n=II()
a=LMIS()

ans=0
for i in range(n):
    if a[i] % 2 == 0:
        a[i]-=1
        ans+=1

for j in a:
    if j % 3 == 2:
        ans+=2

print(ans)