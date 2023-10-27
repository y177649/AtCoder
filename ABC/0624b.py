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
s=[I() for _ in range(n)]

for f1 in range(n):
    for f2 in range(n):
        if f1!=f2:
            origin=s[f1]+s[f2]
            r_origin=origin[::-1]
            if origin==r_origin:
                print('Yes')
                exit()
else:
    print('No')