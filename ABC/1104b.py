'''#中身が一緒かつ、lenと数が同じ時
b=int(input())

ans=[]
for _ in range(10**18):
    b_=b
    if b%2==0:
        b=b//2
        ans.append(2)
    elif b%3==0:
        b=b//3
        ans.append(3)
    else:
        if b!=1:
            ans.append(b)
            break

if len(set(ans))==1 and len(ans)==ans[0]:
    print(ans[0])
else:
    print(-1)

print(ans)
print(len(set(ans)))
print(len(ans))
'''

b=int(input())
for f1 in range(1,18):
    if f1**f1==b:
        print(f1)
        break
else:
    print(-1)