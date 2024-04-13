import cv2 as cv 
import numpy as np 


image = cv.imread('/home/afsal/Desktop/vs_code/afsal_python/open_cv/open_cv_basics/images (1).jpeg')

hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV_FULL)

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# blured_image = cv.bilateralFilter(image, 10, 100, 50)
blured_image = cv.medianBlur(image, 3)

_, thresh = cv.threshold(grey, 100, 255, cv.THRESH_BINARY)

lb, ub = np.array([50, 0, 50], dtype='uint8'), np.array([255, 100, 255], dtype='uint8')

ranged_image = cv.inRange(blured_image, lb, ub)



# thresh = cv.erode(thresh, kernel=np.ones((2, 2)))
eroded_image = cv.erode(ranged_image, kernel=np.ones((1, 1)))

opened_image = cv.morphologyEx(ranged_image, cv.MORPH_CLOSE, np.ones((4, 4)))



gaussian_threshold = cv.adaptiveThreshold(ranged_image, 1, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 3, 1)


cv.imshow('Image', image)
cv.imshow('threshold image', thresh)
cv.imshow('ranged image', ranged_image)
cv.imshow('gaussian_threshold image', gaussian_threshold)
cv.imshow('eroded_image', eroded_image)
cv.imshow('eroded_image', eroded_image)
cv.imshow('opened_image', opened_image)
cv.imshow('hsv', hsv)
cv.waitKey(0)