print('Please enter your availability')

vacant_seat=[] 
for f2 in range(5):
    vacant_seat_input=list(input())
    vacant_seat.append(vacant_seat_input.index('x'))

nop=int(input('Please enter the number of people'))

if nop>=3:
    typ=input('row or box?')
    print(vacant_seat)
    print(nop,'',typ)
else:
    print(vacant_seat)
    print(nop)

sheet='AB CD'

for f1 in range(14):
    if len(str(f1+1))==1:
        print(f1+1,'',sheet)
    else:
        print(f1+1,sheet)