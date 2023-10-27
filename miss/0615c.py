'''
１，全く同じ
２，先頭か末尾に一文字プラス
３，一文字減る
４，一文字入れ替え
'''

n,t=input().split(' ')
n=int(n)
t_=[input() for _ in range(n)]

for f3 in range(n):
    x=t[:f3]+t[f3+1:]
    if x==t_:
        print('Yes')
else:
    print('No')
        

for f2 in range(n):
    if t==t_:
        print('Yes')
        pass
    elif  t==t_[1:] or t==t_[:len(t_)-1]:
        print('Yes')
        pass
    elif 

#print(t[1:],t[:len(t)-1])

print(t3)