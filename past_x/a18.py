x_append=[]

for f1 in range(3):
    x=int(input())
    x_append.append([f1+1,x])

x_append.sort(key=lambda a: a[1])#,reverse=True)

print(x_append)

for f2 in x_append:
    print(f2[0])