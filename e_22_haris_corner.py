import cv2 as cv
import numpy as np 

# use gray scale instead of original
image = cv.imread('images/img.jpg')

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


grayfloat32 = np.float32(gray)

# corner detection the parameters should be almost exact
dst = cv.cornerHarris(grayfloat32, 2, 3, 0.04)

dst = cv.dilate(dst, None)

threshold = 0.01 * dst.max()


image[dst > threshold] = [0, 0, 255]


cv.imshow('Corner Detection', image)
cv.waitKey(0)
cv.destroyAllWindows()