import cv2
import numpy as np
import os

# Function to read images and labels from a directory
def read_images(path, sz=None):
   c = 0
   X, y = [], []
   for dirname, dirnames, filenames in os.walk(path):
      for subdirname in dirnames:
         subject_path = os.path.join(dirname, subdirname)
         for filename in os.listdir(subject_path):
            try:
               im = cv2.imread(os.path.join(subject_path, filename), cv2.IMREAD_GRAYSCALE)
               if sz is not None:
                  im = cv2.resize(im, sz)
               X.append(np.asarray(im, dtype=np.uint8))
               y.append(c)
            except IOError as e:
               print(f"I/O error({e.errno}): {e.strerror}")
            except:
               print("Unexpected error:", os.sys.exc_info()[0])
               raise
         c += 1
   return [X, y]

# Path to the dataset
path = './faces'

# Read the images and labels
[X, y] = read_images(path)
y = np.asarray(y, dtype=np.int32)

# Create the Eigenfaces model
model = cv2.face.EigenFaceRecognizer_create()

# Train the model
model.train(np.asarray(X), np.asarray(y))

# Function to predict the face in an image
def predict(model, image_path):
   img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
   label, confidence = model.predict(img)
   return label, confidence

# Example usage
label, confidence = predict(model, './test_face.jpg')
print(f'Predicted label: {label}, Confidence: {confidence}')