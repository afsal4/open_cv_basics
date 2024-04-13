import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

image = cv.imread('images/img.jpg')

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
p,grey = cv.threshold(image,150, 255, cv.THRESH_BINARY_INV)

print(grey.shape)

kernel = np.ones((2, 2), 'uint8')

dilate = cv.dilate(grey, kernel)
erode = cv.erode(grey, kernel)
open_method = cv.morphologyEx(grey, cv.MORPH_OPEN, kernel)
close = cv.morphologyEx(grey, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(grey, cv.MORPH_GRADIENT, kernel)


images = {'dilate': dilate, 'erode': erode, 'open': open_method, 'close': close, 'grad':gradient}


j = 1
# morphological transformations
for i in images:
    plt.subplot(2, 3, j)
    plt.title(i)
    plt.imshow(images[i], 'gray')
    j += 1
    
plt.show()


# cv.destroyAllWindows()