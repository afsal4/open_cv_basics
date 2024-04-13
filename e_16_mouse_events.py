import cv2 as cv 
import numpy as np 

# printing all the events method 
print([i for i in dir(cv) if i.startswith('EVENT')])
t = False
# this is a specific format for event
def click_event(event, x, y, flags, param):
    global t
    text = f'{x}   {y}'

    if event == cv.EVENT_LBUTTONDOWN:
        t = True
        # print(f'left button down on {x, y}')
        # text = f'{x}   {y}'
        # cv.putText(img, text, (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)
    if event == cv.EVENT_LBUTTONUP:
        t = False
        # print(f'left button down on {x, y}')
        # cv.putText(img, text, (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)
    if event == cv.EVENT_MOUSEMOVE and t:
        cv.circle(img, (x, y),3, (255, 255, 0), -1)
    
    cv.imshow('Image', img)
    


img = np.zeros((512, 512, 3), dtype='uint8')

cv.imshow('Image', img)

cv.setMouseCallback('Image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()