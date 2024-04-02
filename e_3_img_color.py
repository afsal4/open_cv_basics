import cv2 as cv
import numpy as np 
blank_image = np.zeros((500, 500, 3))
blank_image[:] = 0, 255, 0

# cv.imshow('blank', blank_image)
# cv.waitKey(0)
# print(blank_image[:])


# rectangle 
cv.rectangle(blank_image, (20, 100), (340, 400), (255, 255, 255), thickness=cv.FILLED)

# cv.waitKey(0)


# circle 
center = (250, 250)
cv.circle(blank_image, center,radius=50, color=(100, 0, 0), thickness=3)

# line 
cv.line(blank_image, (20, 100), (340, 400), (255, 0, 255), thickness=3)


# write text on an image 
cv.putText(blank_image, 'hello', (225, 225), cv.FONT_HERSHEY_DUPLEX, 1.0, ())
cv.imshow('rectangle', blank_image)
cv.waitKey(0)
