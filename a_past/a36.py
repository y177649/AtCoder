# This is file 36

a,b=list(map(int,input().split()))

for f1 in range(1000):
    if a*(f1+1)>=b:
        break

print(f1+1)