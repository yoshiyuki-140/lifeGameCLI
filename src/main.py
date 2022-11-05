#coding:utf-8

import printWorld as pW
import gameRule
import time

world_size = (10,10)

gR = gameRule.GameOfLife(world_size)
gR.createGlider()

# main
while True:
    pW.printWorld(gR.world)
    gR.update()
    time.sleep(0.5)