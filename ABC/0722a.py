n=int(input())
s=list(input())

a=0
b=0
c=0

for i in range(n):
  
    if s[i]=='A':
        a+=1
    elif s[i]=='B':
        b+=1
    elif s[i]=='C':
        c+=1

    if a>0 and b>0 and c>0:
        print(a+b+c)
        break