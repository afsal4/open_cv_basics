import cv2 as cv 

img = cv.imread('images/hi.png')

vid = cv.VideoCapture('sample_vid/pexels-sapol-chulanol-4629216-3840x2160-24fps.mp4')


def rescale(frame, scale=0.5):
    width = int(frame.shape[1] * 0.3)
    height = int(frame.shape[0] * 0.3)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# scaled_img = rescale(img)

# cv.imshow('img', scaled_img)
# cv.waitKey(0)


while True:
    is_true, frame = vid.read()

    if is_true:
        cv.imshow('vid', rescale(frame))

    if cv.waitKey(20) & 0xFF == ord('d'):
        break 
