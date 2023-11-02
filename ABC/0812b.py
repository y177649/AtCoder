n=int(input())
x=input()

ans=[]

for f1 in range(n):

    c=int(input())
    a=list(map(int,input().split()))

    for f2 in range(c):
        if a[f2] in int(x):
            ans.append(f1)

print(len(ans))
print(ans)
           


'''
4
19
3
19 20
4
19 24 0
2
26 20
3
19 31 24
'''

n=int(input())

for f1 in range(n):
    c=int(input())
    a=list(map(int,input().split()))

x=int(input())