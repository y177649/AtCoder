'''
x=list(input().split('.'))

x0=int(x[0])

x1=list(map(int,(x[1])))

if x1[0]>=5:
    print(x0+1)
else:
    print(x0)

'''


n = input().split('.')
x, y = int(n[0]), int(n[1][0])

print(x + (1 if y >= 5 else 0))