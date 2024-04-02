import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/img.jpg')
cv.imshow('image', img)

# grey scale 
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey scale ', grey)

# bgr to lab 
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# bgr to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)
cv.waitKey(0)



plt.imshow(rgb)
plt.show()
