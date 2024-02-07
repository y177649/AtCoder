h,w,n=list(map(int,input().split()))
ans=[['.' for _ in range(w)] for _ in range(h)]

mx=[-1,0,1,0]
my=[0,1,0,-1]

x,y,m=0,0,0

for _ in range(n):
    if ans[x][y]=='.':
        ans[x][y]='#'
        m=m+1
    else:
        ans[x][y]='.'
        m=m+3

    m=m%4
    x=(x+mx[m])%h
    y=(y+my[m])%w

for result in ans:
    print(''.join(result))