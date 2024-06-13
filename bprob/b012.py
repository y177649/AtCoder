
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

h = n // 3600
a = n % 3600

m = a // 60
s = a % 60

print(f"{h:02}"+':'+f"{m:02}"+':'+f"{s:02}")