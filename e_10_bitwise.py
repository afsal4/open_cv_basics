import cv2 as cv
import numpy as np 

image = cv.imread('images/img.jpg')

blank = np.zeros(image.shape[:2], dtype='uint8')

circle = cv.circle(blank.copy(), (blank.shape[1] // 2, blank.shape[0] // 2), 100, 255, -1)

# mask image should be in binary
mask = cv.bitwise_and(image, image, mask=circle)

cv.imshow('Circle', circle)
cv.imshow('Masked', mask)

# print('circle', circle.shape, 'blank', blank.shape,'image', image.shape,'low_img', image.shape[:2])

cv.waitKey(0)