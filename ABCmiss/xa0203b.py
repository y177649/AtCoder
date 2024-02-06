#input_________

II=lambda:int(input())
MIS=lambda:map(int,input().split())
LMI=lambda:list(map(int,input()))
LMIS=lambda:list(map(int,input().split()))
I=lambda:input()
L=lambda:list(input())
S=lambda:input().split()
#FI=[input() for _ in range(n)]

#code___________

u
if '#' , u == r , x-1 :
    else:
        '.' , u == l , x+1

r
if '#' , r == d ,y-1 :
    else:
        '.' , r == u , y+1

d
if '#' , d == l , x+1 :
    else:
        '.' , d == r , x-1

l
if '#' , l == u , y+1 :
    else:
        '.' , l == d , y-1


H,W,n=MIS()
#print(H,W,N)
li=[W*list('.') for _ in range(H)]
print(li)
y,x,=H-1,W-1
v=['u']
print(x,y)
for i in range(n):
    if li[y][x]=='.':
        li[y][x]='#'
        v='l'


