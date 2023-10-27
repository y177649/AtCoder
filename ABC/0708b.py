#input_________

II=lambda:int(input())
MIS=lambda:map(int,input().split())
LMI=lambda:list(map(int,input()))
LMIS=lambda:list(map(int,input().split()))
I=lambda:input()
L=lambda:list(input())
S=lambda:input().split()

#code___________

n=II()
n_list=[]
for _ in range(n):
    n=I()
    n_list.append(n)