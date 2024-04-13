import cv2 as cv 
import numpy as np 


image_1 = cv.imread('images/img.jpg')
image_2 = cv.imread('images/drawing.jpg')

cv.imshow("Image_1", image_1)
cv.imshow("Image_2", image_2)

# should give col size first rather than row size 
image_2 = cv.resize(image_2, (image_1.shape[1], image_1.shape[0]))


# this wont work if its not in the same size 
added_image = cv.addWeighted(image_1,0.8, image_2, 0.2, 1)

cv.imshow('Added Image', added_image)
cv.waitKey(0)