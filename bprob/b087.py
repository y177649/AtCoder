
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

a = II()
b = II()
c = II()
x = II()
 
#print(a,b,c,x)

result = 0

for loop_a in range(a+1):
    for loop_b in range(b+1):
        for loop_c in range(c+1):
            if loop_a * 500 + loop_b * 100 + loop_c * 50 == x:
                 result += 1

print(result)