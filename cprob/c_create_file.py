for i in range(1, 370):
    filename = f"c{i:03}.py"  # ファイル名を b001.py, b002.py, ... のように生成
    with open(filename, 'w') as file:
        # ファイルに書き込む内容を追加
        content = """# ========== input ===========

II=lambda:int(input())
MIS=lambda:map(int,input().split())
LMI=lambda:list(map(int,input()))
LMIS=lambda:list(map(int,input().split()))
I=lambda:input()
L=lambda:list(input())
S=lambda:input().split()
#FI=[input() for _ in range(n)]

# ========== source code ===========
"""
        file.write(content)