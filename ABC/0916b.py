'''x=input()

x_ans=[]
xs_ans=[]

for f2 in range(len(x)):
    x_ans.append(x[f2:])
    xs_ans.append(x[:-f2])
    """print(x[f2:])
    print(x[:-f2])"""

x_ans_r=[item[::-1] for item in x_ans]
xs_ans_r=[item1[::-1] for item1 in xs_ans]


ans=[]

for x_ans,x_ans_r in zip(x_ans,x_ans_r):
    if x_ans==x_ans_r:
        ans.append(len(x_ans))

for xs_ans,xs_ans_r in zip(xs_ans,xs_ans_r):
    if xs_ans==xs_ans_r:
        ans.append(len(xs_ans))

print(max(ans))
"""print(x_ans)
print(xs_ans)
print(x_ans_r)
print(xs_ans_r)"""
'''


#GPT
x = input()

def is_palindrome(s):
    return s == s[::-1] #True or False

max_length = 0

for i in range(len(x)):
    for j in range(i + 1, len(x) + 1):
        substring = x[i:j]
        if is_palindrome(substring) and len(substring) > max_length:
            max_length = len(substring)

print(max_length)