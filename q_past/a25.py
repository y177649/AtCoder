s=list(input())

#print(s)

s_list=[]

n=int(input())

for f1 in range(len(s)):
    for f2 in range(len(s)):
        s_list.append(s[f1]+s[f2])

#print(s_list)

print(s_list[n-1])