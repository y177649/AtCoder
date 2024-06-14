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

n = II()
a = LMIS()

count = n
for i in range(n) :
    if a[i] == 0 :
        count -= 1

ans = sum(a)//count
#dev = sum(a) % count

if sum(a) % count != 0 :
    ans += 1

print(ans)
#print(sum(a))
#print(dev)