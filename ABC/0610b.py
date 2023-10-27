p,q=map(str,input().split()) #map(str)は何故必要？
c={'A':0,'B':3,'C':4,'D':8,'E':9,'F':14,'G':23} #文字と値を関連付けるために辞書型を使う
print(abs(c[q]-c[p]))