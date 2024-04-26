N, L, R = map(int,input().split())
A = list(map(int,input().split()))
X = []
for i in range(N):
    a = A[i]
    if a <= L:
        X.append(L)
    elif a >= R:
        X.append(R)
    else:
        X.append(a)
print(*X)
#print(X)