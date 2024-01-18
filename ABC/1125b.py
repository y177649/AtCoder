n,l,r=list(map(int,input().split()))

a=list(map(int,input().split()))

list_ans=[]
for f1 in range(n):
    if l<=a[f1]:
        list_ans.append(l)
    elif a[f1]<=r:
        list_ans.append(r)