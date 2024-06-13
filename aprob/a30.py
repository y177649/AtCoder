ao,b,tak,d=list(map(int,input().split()))

aoki=b/ao
takahasi=d/tak

if aoki==takahasi:
    print('DRAW')
elif aoki>takahasi:
    print('TAKAHASHI')
else:
    print('AOKI')

#print(aoki)
#print(takahasi)