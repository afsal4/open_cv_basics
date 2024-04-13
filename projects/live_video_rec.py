import cv2 as cv

video = cv.VideoCapture(-1)

model = cv.CascadeClassifier('haar_ff_tree.xml')


while True:

    ret, frame = video.read()

    # clearing noise 
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # adaptive thresholding 
    thresh_img = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 3, 3)

    cv.imshow('threshold', grey)
    # cv.waitKey(0)

    faces = model.detectMultiScale(thresh_img, 1.1, 1)

    rect = frame
    for (x, y, w, h) in faces:
        rect = cv.rectangle(rect, (x, y), (x+w, y+h), (0, 255, 0), 3)
    

    cv.imshow('video', rect)

    key = cv.waitKey(1)
    if key & 0xFF == ord('g'):
        break

video.release()
cv.destroyAllWindows()