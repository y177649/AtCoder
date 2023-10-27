'''n,m=map(int,input().split())
c=input().split()
d=input().split()
p=list(map(int,input().split()))

total_price=0

for dish in c:
    if dish in d:
        total_price+=p[d.index(dish)+1]
    else:
        total_price+=p[0]

print(total_price)
リストとリストを対応させたいときの使い方＠１０行目
'''

