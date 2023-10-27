x={'R':10,'O':20,'B':30}

print(x)
print(type(x))

print(x.keys()) #キーだけを出力
print(x.values()) #バリューだけを出力

print(x['R']) #Rのバリューを出力、多分一番使う

x['B']=100 #Bのバリューを上書き
print(x)

x['S']=40 #新しいキーとバリューを追加
print(x)

y={'M':50,'N':60} #yの要素をxに追加　辞書型版appendみたいな感じ
x.update(y)
print(x)

print('R' in x) #x辞書の中にRがあるかどうかあればT、なければF

z=('R') #21行と同じ、代入でも可能
print(z in x)