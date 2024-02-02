#参考コード
"""
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())
"""

rm=lambda:map(int,input().split())
rr=lambda:input()

n, m = rm()
s = [rr() for _ in range(n)]
for i in range(n - 8):
    for j in range(m - 8):
        if (
            s[i][j : j + 4] == "###."
            and s[i + 1][j : j + 4] == "###."
            and s[i + 2][j : j + 4] == "###."
            and s[i + 3][j : j + 4] == "...."
        ):
            if (
                s[i + 5][j + 5 : j + 9] == "...."
                and s[i + 6][j + 5 : j + 9] == ".###"
                and s[i + 7][j + 5 : j + 9] == ".###"
                and s[i + 8][j + 5 : j + 9] == ".###"
            ):
                print(i + 1, j + 1)

#print(s)