import numpy as np 
import matplotlib.pyplot as plt
import cv2 as cv


img = cv.imread('images/img.jpg')
cv.imshow('Image', img)

# splitting
b, g, r = cv.split(img)

blank = np.zeros(b.shape, dtype=np.uint8)

print(img.shape, b.shape, g.shape, r.shape, blank.shape, sep="\n")


# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])



cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


cv.waitKey(0)
