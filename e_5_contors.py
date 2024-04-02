import cv2 as cv 
import numpy as np 

img = cv.imread('images/img.jpg')
cv.imshow('image', img)

# bluring the image 
blur = cv.blur(img, (6, 6))
cv.imshow('blurred', blur)

# canny edge detection 
canny = cv.Canny(blur, 200, 200)
cv.imshow('edge', canny)

# finding the contors 
contor, threshold = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# finding the contor in other way 
# greyscaling 
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', grey)

# threshold 
ret, img_threshold = cv.threshold(grey, 200, 255, type=cv.THRESH_BINARY)
cv.imshow('threshold', img_threshold)

contor_1, threshold_1 = cv.findContours(img_threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# drawing_contors  
blank = np.zeros(img.shape)
cv.drawContours(blank, contor_1, -1, (45, 23, 64), 1)
cv.imshow('contor', blank)

print(len(contor),len(contor_1))
# print(contor)



cv.waitKey(0)