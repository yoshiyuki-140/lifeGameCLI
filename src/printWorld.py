#coding:utf-8
# Author : Yoshiyuki Kurose

# - printWorldについて
# worldの内容をCLIに表示する関数
# 引数worldは2次元配列

# - deleteWorldについて
# printWorld関数で標準出力に出力された内容をすべて削除する関数
# 引数world_sizeはindex0番目にworldのwidth,index1番目にworldのheightが入っている

import doctest


def printWorld(world:list):
    """
    """
    print('\x1b[2J')    # ANSIエスケープコードによる画面全体の削除コード
    for row in world:
        for b in row:
            if b == None:
                raise ValueError("b must be bool value")
            if b:
                print('x',end='')
            else:
                print('.',end='')
        print('\n',end='')  # 冗長かもね

    

if __name__ == "__main__":
    doctest.testmod()