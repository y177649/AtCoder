n,l=list(map(int,input().split()))
"""
list_a=[]
for _ in range(n):
    a=int(input())
    list_a.append(a)
"""

list_a=sorted(list(map(int,input().split())))

#list_a=sort()
#print(list_a)

for f1 in range(n):
    if list_a[f1]>=l:
        print(n-f1)
        break
else:
    print(0)