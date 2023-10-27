# This is file 37

h,g,m=list(map(int,input().split()))

if h<=g:
    low=h
else:
    low=g

print(m//low)