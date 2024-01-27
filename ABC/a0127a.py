'''
print(ord('A'),ord('Z'),ord('a'),ord('z'))

add=[]
y=65
for f2 in range(25):
    add.append(chr(y))
    y=y+1
print(add)
'''

x=input()
#print(len(x))

if ord(x[0])>=65 and ord(x[0])<=90:
    #print('y')
    for f1 in range(1,len(x)):
        if ord(x[f1])<=90: #and ord(x[f1])>=65:
            print('No')
            break
    else:
        print('Yes')
else:
    print('No')