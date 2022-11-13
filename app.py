# from PIL.Image import NONE
import cv2
from PIL import ImageGrab
import numpy as np
import pyautogui as pag

from core import Object, grabScreen

player_index = 0
enemy_index = 0

player = [Object('assets/dino.png'), Object('assets/dino_b.png')]
enemies = [
    [Object('assets/cact1.png'), Object('assets/cact2.png'), Object('assets/bird.png')], 
    [Object('assets/cact1_b.png'), Object('assets/cact2_b.png'), Object('assets/bird_b.png')]
    ]

while 1:
    img = grabScreen()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if player[0].match(img):
        topleft_x = int(player[0].location[0][0] - player[0].width)
        topleft_y = int(player[0].location[0][1] - 3*player[0].height)
        bottomright_x = int(player[0].location[1][0] + 14*player[0].width)
        bottomright_y = int(player[0].location[1][1] + 0.5*player[0].height)
        screenStart = (topleft_x, topleft_y)
        screenEnd = (bottomright_x, bottomright_y)
        break

pag.press('space')

while 1: # infinite loop
    img = grabScreen(bbox=(*screenStart, *screenEnd)) # bbox specifies specific region (bbox= x,y,width,height *starts top-left)
    cv2.imshow("Screen", img) # show image on screen
    if cv2.waitKey(1) == ord('q'): # q to quit
        # cv2.destroyAllWindows()
        break
