n = int(input())

lis=[j+1 for j in range(n)]

for i in range(1,len(lis)+1):
    for k in range(1,i+1):
        print(k,end='')
    print()

"""ans
1
12
123
1234
12345
"""