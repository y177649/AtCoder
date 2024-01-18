l,r=map(int,input().split())

s=list(input())

x=s[l-1:r]

ans1=s[:l-1]

ans2=x[::-1]

ans3=s[r:]

print(''.join(ans1+ans2+ans3))