def b_sort(x):
    ans=[]
    for i in range(0,len(x)-1,2):
        if x[i]<x[i+1]:
            ans.append(x[i])
            ans.append(x[i+1])
        else:
            ans.append(x[i+1])
            ans.append(x[i])
    return ans

x=list(map(int,input().split()))

print(b_sort(x))