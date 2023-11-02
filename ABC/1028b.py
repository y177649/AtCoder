n=list(map(int,input()))

for f1 in range(919):
    if n[0]*n[1]==n[2]:
        ans=''.join([str(f2) for f2 in n])
        print(ans)
        break
    else:
        int_n=int(''.join([str(f3) for f3 in n]))
        int_n+=1
        str_n=str(int_n)
        n_=[]
        for f4 in range(3):
            n_.append(int(str_n[f4]))
        n=n_