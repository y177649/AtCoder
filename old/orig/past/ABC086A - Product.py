a,b=list(map(int,input().split()))

pri='Even'

ab=a*b

if ab%2==1:
    pri='Odd'

print(pri)