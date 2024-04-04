import cv2 as cv 
import numpy as np 

image = cv.imread('images/img.jpg')

# converting to binary using grey scale 
grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# simple threshold 
thresh_val, thresh = cv.threshold(grey, 150, 255, cv.THRESH_BINARY)

# inverse threshold 
thresh_inv_val, thresh_inv = cv.threshold(grey, 150, 255, cv.THRESH_BINARY_INV)


# adaptive mean threshold 
adapt_thresh = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 36)

adapt_thresh_inv = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 3, 36)

adapt_thresh_gauss = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 5, 5)

print(adapt_thresh.shape)
cv.imshow('Simple Threshold', thresh)
cv.imshow('Simple Inverse Threshold', thresh_inv)
cv.imshow('Adaptive Threshold', adapt_thresh)
cv.imshow('Adaptive Inverse Threshold', adapt_thresh_inv)
cv.imshow('Gaussian Adaptive Inverse Threshold', adapt_thresh_gauss)

cv.waitKey(0)