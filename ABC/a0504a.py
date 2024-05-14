n,x,y,z=map(int,input().split())

pri="No"

if x<z and y>z or y<z and x>z:
    pri="Yes"

print(pri)
