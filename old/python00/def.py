def pri_b():
    print('b')

pri_b()

def pri_t(t):
    print(t)

pri_t('apple')

def question_text(text):
    text_q=text + '?'
    return text_q

result_t = question_text('apple')
print(result_t)

def qe_text(q,e):
    text_q = q + '?'
    text_e = e + '!'
    return text_q,text_e

r1,r2 = qe_text('apple','banana')
print(r1)
print(r2)


def printHelloWord():
    print('Hello Word!')

printHelloWord()


def add(n1,n2):
    print(n1+n2)

add(1,2)


def add(n1,n2):
    return(n1+n2)

print(add(2,3))


def add(n1,n2):
    return(n1+n2)

add_result=add(3,4)
print(add_result)


a,b,c=map(int,input().split())

def av(a,b,c):
    print((a+b+c)/3)

av(a,b,c)