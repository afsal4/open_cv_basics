import cv2 as cv
import numpy as np 
import os 

DIR = 'train/'
haar_cascade = cv.CascadeClassifier('haar_ff_tree.xml')

person = ['Madonna', 'Ben Afflek', 'Elton John', 'Mindy Kaling', 'Jerry Seinfield']


def detect_faces(dir_path):
    '''function to detect faces'''
    image_names = os.listdir(dir_path)

    faces = {}

    for image_path in image_names:
        image = cv.imread(os.path.join(dir_path, image_path))
        grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        res = haar_cascade.detectMultiScale(grey, 1.1, minNeighbors=1)
        if len(res) > 0:
            faces[image_path] = res
    return faces

# draws rectangle over detected faces 
def draw_rectangle(faces, path):
    for image in faces:
        img = cv.imread(os.path.join(path, image))
        for (x, y, w, h) in faces[image]:
            rect = cv.rectangle(img, (x, y), (w+x, h+y), (0, 255, 0), 3)
            rect = cv.resize(rect, (img.shape[1] // 2, img.shape[0] // 2))
            cv.imshow('Detected Faces', rect)



people, labels = [], []

def crop_faces(path):
    global people, labels
    faces = detect_faces(path)
    print(path)

    i = 0
    for image in faces:
        img = cv.imread(os.path.join(path, image))

        grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        for (x, y, w, h) in faces[image]:
            crop_face = grey[y:y+h, x:x+w]
            people.append(crop_face)

            label = person.index(path.split('/')[-1])
            labels.append(label)

            # cv.imshow(f'cropped face{i}', crop_face)
            i += 1

def train_faces(path):
    global people, labels

    people = np.array(people, dtype='object')
    labels = np.array(labels)
    print(type(labels), type(people), people.shape, labels.shape)


    face_recognition  = cv.face.LBPHFaceRecognizer.create()
    face_recognition.train(people, labels)

    face_recognition.save('trained.yml')



# faces = detect_faces(images, 'images/')
# draw_rectangle(faces)












for i in person:
    path = os.path.join(DIR, i)
    crop_faces(path)

train_faces(path)
print()

# test_dir = 'val/'
# test_label = os.listdir(test_dir)


print(person)

cv.waitKey(0)
cv.destroyAllWindows()


