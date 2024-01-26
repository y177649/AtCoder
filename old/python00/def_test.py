x=list(input().split())

def kaibun(text):
    if text==text[::-1]:
        res='Yes'
    else:
        res='No'
    return res

#result=kaibun(x)

for f1 in range(len(x)):
    if kaibun(x[f1])=='No':
        print('No')
        break
else:
    print('Yes')

#print(result)

'''
for f1 in range(len(x)):
    for_x=x[f1]
    if for_x!=for_x[::-1]:
        print('No')
        break
else:
    print('Yes')
'''