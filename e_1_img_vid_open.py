import cv2 as cv

# # converts the image to np arrays
# img = cv.imread('images/hi.png')

# cv.imshow('somehing', img)

# print(img.shape)

capture = cv.VideoCapture('sample_vid/pexels-sapol-chulanol-4629216-3840x2160-24fps.mp4')

while True:
    is_true, frame = capture.read()
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()