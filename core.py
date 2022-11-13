import cv2
from PIL import ImageGrab
import numpy as np

# class Object:
#     def __init__(self, path):
#         img = cv2.imread(path, 0)
#         self.img = img
#         self.width = img.shape[1]
#         self.height = img.shape[0]
#         self.location = None

#     def match(self, scr):
#         res = cv2.matchTemplate(scr, self.img, cv2.TM_CCOEFF_NORMED) # returns a 2D array of the correlation between the two images
#         # high accuracy is close to 1, low value is close to 0
#         minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res) # returns the location of the highest correlation
#         startLoc = maxLoc
#         endLoc = (startLoc[0] + self.width, startLoc[1] + self.height)  # endLoc is the bottom right corner of the player
#         if maxVal >= 0.8: # if the correlation is high enough
#             self.location = (startLoc, endLoc)
#             return True
#         else:
#             self.location = None
#             return False

class Object:
    def __init__(self, path):
        img = cv2.imread(path, 0)
        self.img = img
        self.width = img.shape[1]
        self.height = img.shape[0]
        self.location = None

    def match(self, scr):
        res = cv2.matchTemplate(scr, self.img, cv2.TM_CCOEFF_NORMED)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
        startLoc = maxLoc
        endLoc = (startLoc[0]+self.width, startLoc[1]+self.height)

        if maxVal>0.8:
            self.location = (startLoc, endLoc)
            return True
        else:
            self.location = None
            return False

def grabScreen(bbox=None):
    img = ImageGrab.grab(bbox=bbox) # bbox specifies specific region (bbox= x,y,width,height *starts top-left)
    img = np.array(img) # this is the array obtained from conversion
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # cv2 reads colors as BGR, convert it to RGB
    return img # returns image