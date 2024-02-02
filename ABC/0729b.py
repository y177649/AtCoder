#input_________

II=lambda:int(input())
MIS=lambda:map(int,input().split())
LMI=lambda:list(map(int,input()))
LMIS=lambda:list(map(int,input().split()))
I=lambda:input()
L=lambda:list(input())
S=lambda:input().split()
#FI=[input() for _ in range(n)]

#code___________

n,m=MIS()
#print(n,m)

ls=[]
for f1 in range(n):
    s=input()
    ls.append(s)
#print(ls)

for f2 in range(n-8):
    for f3 in range(m-8):

        if (ls[f2][f3:f3+4]=='###.'
            and ls[f2+1][f3:f3+4]=='###.'
            and ls[f2+2][f3:f3+4]=='###.'
            and ls[f2+3][f3:f3+4]=='....'
        ):

            if (ls[f2+5][f3+5:f3+9]=='....'
                and ls[f2+6][f3+5:f3+9]=='.###'
                and ls[f2+7][f3+5:f3+9]=='.###'
                and ls[f2+8][f3+5:f3+9]=='.###'
            ):
                print(f2+1,f3+1)