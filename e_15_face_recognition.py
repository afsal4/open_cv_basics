import cv2 as cv 
import numpy as np 
import os 
face_recognizer  = cv.face.LBPHFaceRecognizer().create()
face_recognizer.read('trained.yml')

testing_dir  = 'val/'

people = ['madonna', 'ben_afflek', 'elton_john', 'mindy_kaling', 'jerry_seinfeld']

face_detection = cv.CascadeClassifier('haar_ff_tree.xml')

def crop(faces, image):
    x, y, w, h = faces
    cropped = image[y:y+h, x:x+w]
    return cropped


def face_prediction(images, labels):
    # converting to array 
    labels = np.array(labels)
    images = np.array(images, dtype='object')

    accuracy = np.zeros(labels.shape)
    i = 0

    for (image, label) in zip(images, labels):
        res, confidence = face_recognizer.predict(image)
        if res == label:
            accuracy[i] = 1
        i += 1
        print(f'actual {people[label]}, prediction {people[int(res)]} with confidence of {confidence}')
    print(accuracy.mean()) 
    return accuracy.mean()

def test(path, people, minn):
    label = []
    test_images = []

    for person in people:

        folder_path = os.path.join(path, person)

        for image in os.listdir(folder_path):
            img = cv.imread(os.path.join(folder_path, image))
            grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            faces_detected = face_detection.detectMultiScale(grey, 1.1, minn)

            for face in faces_detected:

                cropped_face = crop(face, grey)

                test_images.append(cropped_face)
                label.append(people.index(person))

    return face_prediction(test_images, label)


test(testing_dir, people, 1)
