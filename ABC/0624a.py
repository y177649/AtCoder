n=int(input())
a=list(map(int,input().split()))

for i in range(0, len(a), 7):
    print((sum(a[i:i+7])),end=' ')