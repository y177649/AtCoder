n,m=list(map(int,input().split()))
s=input()
t=input()

len_s=len(s)
t_len_s=len(t)-len_s

'''print(len_s)
print(t[:len_s])
print(t[t_len_s:])'''

if t[:len_s]==s and t[t_len_s:]==s:
    print(0)
elif t[:len_s]==s:
    print(1)
elif t[t_len_s:]==s:
    print(2)
else:
    print(3)