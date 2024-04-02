import cv2 as cv
import numpy as np 
img = cv.imread('images/hi.png')

img = cv.resize(img, dsize=(img.shape[0] // 1, img.shape[1] // 1))

# translate  
def translate(img, x, y):
    trans_met = np.float32([[1, 0, x], [0, 6, y]])
    dimensions = img.shape[1], img.shape[0]
    print(trans_met)
    return cv.warpAffine(img, trans_met, dimensions)

# -x = left 
#  x = right 
# -y = up 
#  y = down


translated_img = translate(img, 100, 100)
cv.imshow('Translated', translated_img)

def rotate(img, angle, rotPoint= None): 
    if rotPoint==None:
        rotPoint = (img.shape[0]//2, img.shape[1]//2)
    rot_mat = cv.getRotationMatrix2D(rotPoint, (angle), 1.0)
    return cv.warpAffine(img, rot_mat, (img.shape[1], img.shape[0]))

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)
cv.waitKey(0)

# negative values for anticlock wise rotation 

# flipping
flip = cv.flip(img, 0)

# 0, 1, -1 (args) vertically, horizondally, both

