import cv2 as cv 
import numpy as np 


blank = np.zeros((500, 500, 3), dtype='uint8')

def change(x):
    # print(x)
    ...

cv.namedWindow('Image')

cv.createTrackbar('B', 'Image', 0, 255, change)
cv.createTrackbar('G', 'Image', 0, 255, change)
cv.createTrackbar('R', 'Image', 0, 255, change)


while True:
    b = cv.getTrackbarPos('B', 'Image')
    g = cv.getTrackbarPos('G', 'Image')
    r = cv.getTrackbarPos('R', 'Image')

    blank[:] = [b, g, r]
    print('blank', blank[:, 0])

    cv.imshow('Image', blank)


    if cv.waitKey(1) & 0xff == ord('d'):
        break
