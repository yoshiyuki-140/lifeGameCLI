#coding:utf-8

import gameRule
import time
from outputUtil import printWorld

world_size = (10, 10)
generation = 10
delay = 0.5

gR = gameRule.GameOfLife(world_size)
gR.createGlider()

print('\n'*world_size[1])    # 画面の高さ分の改行

# main
for _ in range(generation):
    printWorld(gR.world)
    gR.update()
    time.sleep(delay)
