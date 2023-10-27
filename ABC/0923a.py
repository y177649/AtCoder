'''n=list(map(int,input()))

pri='x'

if len(n)==1:
    pri='Yes'

for f1 in range(len(n)-1):

    if n[f1]>n[f1+1]:
        pri='Yes'
    else:
        pri='No'

print(pri)'''

#input_________

I=lambda:int(input())
MIS=lambda:map(int,input().split())
LMI=lambda:list(map(int,input()))
LMIS=lambda:list(map(int,input().split()))
L=lambda:list(input())
S=lambda:input().split()

#code___________

n=LMI()
#print(len(n))
if len(n)==1:
    print('Yes')
else:
    cou=0
    for f1 in range(len(n)-1):
        if n[f1]-n[f1+1]>0:
            cou+=1

    if cou==len(n)-1:
        print('Yes')
    else:
        print('No')

    #print(cou,len(n)-1)