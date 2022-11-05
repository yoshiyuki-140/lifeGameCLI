#coding:utf-8
# Author : Yoshiyuki Kurose

from copy import deepcopy
from random import choice

# Game rules
class GameOfLife:
    """
    このライフゲームの要となる法則を定義している。
    """

    def __init__(self, world_size: tuple):
        #世界の大きさdefoultで10
        self.world_size = world_size
        self.allDeath() # ここでself.worldクラス変数が定義される
        self.tmp_world = deepcopy(self.world)
        self.count = 0

    def allDeath(self):
        """
        """
        self.world = [[False for _ in range(
            self.world_size[0])] for _ in range(self.world_size[1])]


    def update(self):
        """世代交代
        """
        self.tmp_world = deepcopy(self.world)
        for y in range(self.world_size[1]):
            for x in range(self.world_size[0]):
                self.tmp_world[y][x] = self.judge(x, y)
        self.world = deepcopy(self.tmp_world)

    def createGlider(self):
        """conway's game of life における グライダーを作成する
        """

        self.world[1][1] = True
        self.world[1][2] = False
        self.world[1][3] = True
        self.world[2][1] = False
        self.world[2][2] = True
        self.world[2][3] = True
        self.world[3][1] = False
        self.world[3][2] = True
        self.world[3][3] = False

    def chaosWorld(self):
        """世界の状態をカオスに初期化する
        """
        self.world = [[choice([True, False]) for _ in range(
            self.world_size[0])] for _ in range(self.world_size[1])]

    def toggleCell(self, x, y):
        """ ガウス平面の (x,y)座標 として扱え
        Args:
            x (int): 座標データなので1以上
            y (int): 座標データなので1以上
        """
        self.world[y-1][x-1] = not self.world[y-1][x-1]

    def judge(self, x, y):
        """次の時代lifeならTrueを返すdeathならFalseをかえす
        """

        self.countCells(x, y)
        # 最後のジャッジ変更した
        if self.world[y][x]:
            if self.count == 2 or self.count == 3:
                return True
            return False
        else:
            if self.count == 3:
                return True
            return False
        

    def countCells(self, x, y):
        """周辺の状態をカウントする
        """
        self.count = 0
        if self.world[(y-1) % self.world_size[1]][(x-1) % self.world_size[0]] == True:
            self.count += 1
        if self.world[(y-1) % self.world_size[1]][(x) % self.world_size[0]] == True:
            self.count += 1
        if self.world[(y-1) % self.world_size[1]][(x+1) % self.world_size[0]] == True:
            self.count += 1
        if self.world[(y) % self.world_size[1]][(x-1) % self.world_size[0]] == True:
            self.count += 1
        if self.world[(y) % self.world_size[1]][(x+1) % self.world_size[0]] == True:
            self.count += 1
        if self.world[(y+1) % self.world_size[1]][(x-1) % self.world_size[0]] == True:
            self.count += 1
        if self.world[(y+1) % self.world_size[1]][(x) % self.world_size[0]] == True:
            self.count += 1
        if self.world[(y+1) % self.world_size[1]][(x+1) % self.world_size[0]] == True:
            self.count += 1
        return self.count
