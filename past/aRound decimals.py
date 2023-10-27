x=list(input())

xx=x[:len(x)-4]

xxx=[int(i) for i in xx]
print(xxx)

xxxx=int(xxx[0])

#x3=int(x[-1])
#x2=int(x[-2])
x1=int(x[-3])

#if x3>=5:
#    x2+=1
#if x2>=5:
#    x1+=1
if x1>=5:
    xxx+=1

print(xxx)