import cv2
from core import Object

player = Object('assets/dino.png')
scr = cv2.imread('assets/screen.png', 0)

location = match(scr, player)

# draw a rectangle around the player
scr = cv2.cvtColor(scr, cv2.COLOR_GRAY2RGB)
cv2.rectangle(scr, location[0], location[1], (255, 0, 0), 2)

cv2.imshow('res', scr) # show the correlation array, white is high correlation, black is low correlation
cv2.waitKey(0)
