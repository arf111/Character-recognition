import os
import numpy as np
import cv2
import pickle
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.externals.joblib import dump, load
from skimage.feature import hog

X = []
y = []
winSize = (30,30)

for path, subdirs, files in os.walk('dataset/English/Img/GoodImg/Bmp/'):
    for filename in files:
        f = os.path.join(path, filename)  # filename: 'img001-0004.png'
        target = filename[3:filename.index('-')]  # target: 001
        img = cv2.imread(f, 0)  # load a color image into greyscale image

        img_hog = hog(img)
        print(img_hog.shape)

#             if img.shape[0] <= 30 or img.shape[1] <= 30:
#                 continue
#             img_resized = cv2.resize(img,(30,30))
#             img_resized = hog.compute(img_resized)

        X.append(img_hog)
        y.append(target)

# Shape [5311, 900, 1] => 5311 ta sample, 900(30x30) hocche pixel values
X = np.array(X)
print(X.shape)
