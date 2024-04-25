import os
import cv2
import numpy as np
from PIL import Image


recognizer = cv2.face.LBPHFaceRecognizer_create()
path = "dataset"

def get_images_with_id(path):
    images_paths = [os.path.join(path,f) for f in os.listdir(path)]
    faces = []
    ids = []
    for single_image_path in images_paths:
        faceImage = Image.open(single_image_path).convert('L')
        faceNp = np.array(faceImage,np.uint8)
        id = int(os.path.split(single_image_path)[-1].split(".")[1])
        print(id)
        faces.append(faceNp)
        ids.append(id)
        cv2.imshow("traning", faceNp)
        cv2.waitKey(100)

    return np.array(ids), faces

ids, faces = get_images_with_id(path)
print(faces, ids)
labels = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
recognizer.train(faces, ids)
recognizer.save("Reco/trained.yml")
cv2.destroyAllWindows()

