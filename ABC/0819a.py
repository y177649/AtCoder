#input_________

II=lambda:int(input())
MIS=lambda:map(int,input().split())
LMI=lambda:list(map(int,input()))
LMIS=lambda:list(map(int,input().split()))
I=lambda:input()
L=lambda:list(input())
S=lambda:input().split()

#code___________

s=L()
#print(s)
#vowel=['a','e','i','o','u']

ans=[]
for f1 in range(len(s)):
    if s[f1]!='a' and s[f1]!='e' and s[f1]!='i' and s[f1]!='o' and s[f1]!='u':
    #if s[f1] not in ['a','e','i','o','u']:
        ans.append(s[f1])

print(''.join(ans))