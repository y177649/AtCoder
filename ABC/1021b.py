n=int(input())

wx_list=[]
for f1 in range(n):
    wx=list(map(int,input().split()))
    wx_list.append(wx)

wx_sort=sorted(wx_list,key=lambda x:x[1])

wx_sort_list=[list(wx_in) for wx_in in wx_sort]

print(wx_sort_list,'debug')
'''
ans=[]
for f3 in range(n-1):
    for f4 in range(n-1):
        if wx_sort_list[f3][1]+wx_sort_list[f4][1]<=9:
            ans.append(wx_sort_list[f3][0]+wx_sort_list[f4][0])

#print(max(ans))

ans_=[]
for f5 in range(n):
    if ans[f5]<=9:
        ans_.append(ans[f5])
    
print(max(ans_))
'''

wx_add=[]
for f3 in range(n):
    for f4 in range(n):
        wx_add.append(wx_sort_list[f3:f4+1])

wx_f5_add=[]
for wx_f5 in wx_add:
    if wx_f5:
        wx_sum_f5=sum(wx_f5)
        wx_f5_add.append(wx_sum_f5)
    else:
        wx_f5_add.append(0)


print(wx_f5_add)
'''
for debug in wx_add:
    print(debug)'''