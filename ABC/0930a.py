'''n=int(input())

s=input()

for f1 in range(n):
    if s[f1:f1+2]=='ABC':
        print(f1)
        break
    else:
        print('-1')

#x='ABABCABC'
#print(x[0:2])
'''

#input_________

INT=lambda:int(input())
MI=lambda:map(int,input().split())
LMI=lambda:list(map(int,input().split()))
LI=lambda:list(input())
IS=lambda:input().split()

#code___________
s=INT()
n=LI()
#print(n)
for f1 in range(len(n)-2):
    if n[f1]=='A' and n[f1+1]=='B' and n[f1+2]=='C':
        print(f1+1)
        break
else:
    print(-1)