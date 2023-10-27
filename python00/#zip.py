n=['py','ruby','php']
m=[10,100,1000]

print(zip(n,m))
print(type(zip(n,m)))

for i in zip(n,m):
    print(i)

print()

for j,b in zip(n,m):
    print(j)
    print(b)