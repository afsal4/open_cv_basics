import cv2 as cv
import numpy as np 



img = cv.imread('images/cat.jpeg')

cv.namedWindow('Image')

cv.createTrackbar('hl', 'Image', 0, 256, lambda x:x)
cv.createTrackbar('hu', 'Image', 255, 256, lambda x:x)
cv.createTrackbar('sl', 'Image', 0, 256, lambda x:x)
cv.createTrackbar('su', 'Image', 255, 256, lambda x:x)
cv.createTrackbar('vl', 'Image', 0, 256, lambda x:x)
cv.createTrackbar('vu', 'Image', 255, 256, lambda x:x)
cv.createTrackbar('t1', 'Image', 0, 500, lambda x:x)
cv.createTrackbar('t2', 'Image', 0, 500, lambda x:x)

while True:

    hl = cv.getTrackbarPos('hl', 'Image')
    hu = cv.getTrackbarPos('hu', 'Image')
    sl = cv.getTrackbarPos('sl', 'Image')
    # su = cv.getTrackbarPos('su', 'Image')
    su = 33
    # vl = cv.getTrackbarPos('vl', 'Image')
    vl = 43
    vu = cv.getTrackbarPos('vu', 'Image')
    t1 = cv.getTrackbarPos('t1', 'Image')
    t2 = cv.getTrackbarPos('t2', 'Image')

    LB = np.array([hl, sl, vl])
    UB = np.array([hu, su, vu])

    print(LB, UB)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    mask = cv.inRange(img, LB, UB)
    hsv_mask = cv.inRange(hsv, LB, UB)
    mask_not = cv.bitwise_not(mask)
    hsv_mask_not = cv.bitwise_not(mask)
    morph = cv.morphologyEx(hsv_mask, cv.MORPH_OPEN, kernel=np.ones((2, 2)))


    added_image = cv.bitwise_and(img, img, mask=morph)
    hsv_added_image = cv.bitwise_and(hsv, img, mask=hsv_mask)

    blurred = cv.bilateralFilter(added_image, 5, 255, 3)
    canny_edge = cv.Canny(morph, t1, t2)


    cv.imshow('Image', img)
    cv.imshow('added_image', added_image)
    cv.imshow('mask', mask)
    cv.imshow('hsv mask', hsv_mask)
    cv.imshow('hsv added mask', hsv_added_image)
    cv.imshow('mask_not', mask_not)
    cv.imshow('canny_edge', canny_edge)
    cv.imshow('morph', morph)



    if cv.waitKey(1) & 0xff == ord('a'):
        break 
