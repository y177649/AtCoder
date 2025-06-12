n=int(input())
t=list(input())
a=list(input())

#print(t)

for i in range(n):
    if a[i]==t[i] and a[i]=='o':
        print('Yes')
        break
else:
    print('No')