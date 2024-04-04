import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 


image = cv.imread('images/img.jpg')

blank = np.zeros(image.shape[:2], dtype='uint8')

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

circle = cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(grey, grey, mask=circle)

cv.imshow('Masked Image', mask)


# calculating histogram 
grey_hist = cv.calcHist([grey], [0], None, [256], [0, 256])

plt.figure()
plt.plot(grey_hist)
plt.show()

for i, color in enumerate(('b', 'g', 'r')):
    colored_hist = cv.calcHist([image], [i], circle, [256], [0, 256])
    plt.plot(colored_hist, label=f'{color} intensity', color=color)

# print(grey.shape)

plt.title('Colored Image Histogram')
plt.xlabel('Color Intensity')
plt.ylabel('Count')
plt.legend()
plt.show()


cv.waitKey(0)