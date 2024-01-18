print(range(5))
print(type(range(5)))

print()

for i in range(5):   #レンジの（）内は　スタート　ストップ　ステップで　この例では
    print(i)         #スタートの０と、ステップの１を省略している

print()

for j in range(5,10):   #ステップの１を省略している
    print(j)

print()

for b in range(5,10,2):   #省略なし
    print(b)