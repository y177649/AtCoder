n=int(input())

if 54<=n:
    
    if len(str(n))==2:
        print('AGC0',n+1,sep='')
    else:
        print('AGC',n+1,sep='')

elif len(str(n))==1:
    print('AGC00',n,sep='')
else:
    print('AGC0',n,sep='')