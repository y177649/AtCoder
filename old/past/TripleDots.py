k=int(input())
s=list(input())

def sk_check(k,s):
    if k<len(s):
        print(''.join(s[:k])+'...')
    else:
        print(''.join(s))

sk_check(k,s)