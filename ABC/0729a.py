'''s=input()

if s=='ACE' or 'BDF' or 'CEG' or 'DFA' or 'EGB' or 'FAC' or 'GBD':
    print('Yes')
else:
    print('No')'''

#input_________

II=lambda:int(input())
MIS=lambda:map(int,input().split())
LMI=lambda:list(map(int,input()))
LMIS=lambda:list(map(int,input().split()))
I=lambda:input()
L=lambda:list(input())
S=lambda:input().split()

#code___________
s=I()
#print(s)
if  s=='ACE' or s=='BDF' or s=='CEG' or s=='DFA' or s=='EGB' or s=='FAC' or s=='GBD': 
    print('Yes')
else:
    print('No')