import cv2 as cv
import numpy as np

image = cv.imread('images/img.jpg')

# grey scale image 
# blured_image = cv.GaussianBlur(image, (3, 3), 4)

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# laplacian
laplacian = cv.Laplacian(grey, cv.CV_64F)

laplacian = np.uint8(np.absolute(laplacian))

sobel_x = cv.Sobel(image, cv.CV_64F, 0, 1)
sobel_y = cv.Sobel(image, cv.CV_64F, 1, 0)

sobel_x_and_y = cv.bitwise_and(sobel_x, sobel_y)
sobel_x_or_y = cv.bitwise_or(sobel_x, sobel_y)


cv.imshow('Laplacian', laplacian)
cv.imshow('Sobel_X', sobel_x)
cv.imshow('Sobel_Y', sobel_y)
cv.imshow('Sobel_X_and_Y', sobel_x_and_y)
cv.imshow('Sobel_X_or_Y', sobel_x_or_y)
cv.waitKey(0)