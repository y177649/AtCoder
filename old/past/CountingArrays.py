'''n=int(input())

a=[]

for f1 in range(n):
    la=list(map(int,input().split()))
    a.append(int(''.join(map(str,la[1:]))))

print(len(set(a)))
'''

n=int(input())

a=[]

for _ in range(n):
    la=list(map(int,input().split()))[1:]
    a.append(tuple(la))

print(len(set((a))))