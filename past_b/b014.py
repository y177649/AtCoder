
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

n,X=MIS()
a=LMIS()

x_binary=bin(X)[2:].zfill(n)

ans=0
"""
if X == 0:
    print(ans)
else:

    if len(x_binary) != n:
        new_x_binary = "0" + x_binary
    else:
        new_x_binary = x_binary
"""
#dev_ans=[]  
for i in range(n):
    if x_binary[i] == "1":
        ans += a[i-1]
        #dev_ans.append(a[i])

print(ans)
"""
print(dev_ans)
print(a)
print(x_binary)
print(new_x_binary)
"""