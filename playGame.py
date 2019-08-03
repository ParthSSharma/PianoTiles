import numpy as np
import cv2
from directKeys import click, queryMousePosition
import math
from PIL import ImageGrab
import time

rows = 100
cols = [14, 114, 214, 314]
gameCoords = [0, 403, 398, 552]
gameOver = 0
gameWon = 0

def clickTiles(screen):
    global gameOver, gameWon
    for col in cols:
        if screen[rows][col][0] < 18 and screen[rows][col][1] < 18 and screen[rows][col][2] < 18:
            click(col, rows + gameCoords[1])
            print("clicked")
            break
        elif screen[rows][col][0] > 200 and screen[rows][col][1] < 200 and screen[rows][col][2] < 200:
            gameOver = 1
        elif screen[rows][col][0] < 200 and screen[rows][col][1] > 200 and screen[rows][col][2] < 200:
            gameWon = 1

print("Alright, let's move out!")
while True:
    mousePos = queryMousePosition()
    #print(mousePos.x, mousePos.y)
    if mousePos.x <= 300:
        break
    
print("Go, Go, Go!!")
time.sleep(2)
while True:
    mousePos = queryMousePosition()
    if ((gameCoords[0] < mousePos.x < gameCoords[2]) and (gameCoords[1] < mousePos.y < gameCoords[3])):
        screen = np.array(ImageGrab.grab(bbox = gameCoords))
##        print(mousePos.x, mousePos.y)
        #print(screen[mousePos.y - gameCoords[1]][mousePos.x])
        clickTiles(screen)
        time.sleep(0.125)
        if gameOver:
            print("We lost!")
            break
        if gameWon:
            print("We won!")
            break
