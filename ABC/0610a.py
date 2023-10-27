n=int(input())

if n%5<=2:
    print(n//5*5)
else:
    print(n//5*5+5)

#print(n//5*5 if (n:=int(input()))%5<=2 else n//5*5+5)