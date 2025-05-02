N = int(input())
ai = list(map(int,input().split()))

#print(N,ai)

ai.sort(reverse = True)

Alices_points = sum(ai[::2])
Bobs_points = sum(ai[1::2])

"""
for i in range(0 , len(ai)//2 , 1):
    Alices_points + i

for j in range(1 , len(ai)//2 , 1):
    Bobs_points + j

#print(len(ai)//2)
"""

print(Alices_points - Bobs_points)