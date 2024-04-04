import cv2 as cv
import numpy as np 

blank = np.zeros((400, 400))

rectangle = cv.rectangle(blank.copy(), (40, 40), (380, 380), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

bitwise_or = cv.bitwise_or(rectangle, circle)
bitwise_and = cv.bitwise_and(rectangle, circle)
bitwise_xor = cv.bitwise_xor(rectangle, circle)

cv.imshow("Bitwise OR", bitwise_or)
cv.imshow("Bitwise AND", bitwise_and)
cv.imshow("Bitwise XOR", bitwise_xor)

a = cv.imread('images/img.jpg')
b = cv.imread('images/hi.png')

blured_a = cv.bilateralFilter(a, 5, 50, 50)
blured_b = cv.bilateralFilter(b, 20, 125, 125)

cv.imshow('blured a', blured_a)
cv.imshow('blured b', blured_b)

grey = cv.cvtColor(blured_a, cv.COLOR_BGR2GRAY)


edge_a = cv.Canny(blured_a, 100, 150)
edge_b = cv.Canny(blured_b, 100, 150)

rec, thresh = cv.threshold(grey, 200, 255, cv.THRESH_BINARY)

cv.imshow('edge a', edge_a)
cv.imshow('edge b', edge_b)


cv.imshow('thresh b', thresh)



# cv.imshow("Bitwise OR", cv.bitwise_or(a, b))


cv.waitKey(0)