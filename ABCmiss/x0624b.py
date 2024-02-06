#input_________

II=lambda:int(input())
MIS=lambda:map(int,input().split())
LMI=lambda:list(map(int,input()))
LMIS=lambda:list(map(int,input().split()))
I=lambda:input()
L=lambda:list(input())
S=lambda:input().split()

#code___________

n=II()
#print(n)
all_list=[]
for f1 in range(n):
    s=I()
    all_list.append(s)

combo_list=[]
for f2 in range(n):
    for f3 in range(n):
        if f2!=f3:
            combo_list.append(all_list[f2]+all_list[f3])
#print(combo_list)

r_combo_list=[f5[::-1] for f5 in combo_list]
#print(r_combo_list)

for f4 in range(n):
    if combo_list[f4]==r_combo_list[f4]:
        print('Yes')
        break