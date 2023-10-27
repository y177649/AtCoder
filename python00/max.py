x=[1,2,3,4,5]
print(max(x)) #最大値をプリント
print(min(x)) #最小値をプリント

y=['python','javascript','php']
print(max(y,key=len)) #文字数の１番大きいものをプリント

z={'a':3,'b':2,'c':1}
print(max(z)) #keyの１番大きいものをプリント
print(max(z.values())) #valuesの一番大きいものをプリント