se=0

for f1 in range(3):
    s,e=list(map(int,input().split()))
    se+=s*(e*0.1)//1

print(int(se))