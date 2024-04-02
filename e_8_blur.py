import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 


img = cv.imread('images/img.jpg')

blur = cv.blur(img, (7, 7))
cv.imshow('Normal blur', blur)

# gaussian blur less blur than normal
gaussian_blur = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussain Blur', gaussian_blur)

# median blur removes most noise 
median_blur = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median_blur)

# bilateral
bil = cv.bilateralFilter(img, 20, 100, 100)
cv.imshow('Bilateral', bil)

cv.imshow('Normal', img)

cv.waitKey(0)