import pandas as pd
from fixdata import fixData
from mlAlgos import *

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

#testData, trainData, trainSurvived, passengerId = fixData("testdata/train.csv", "testdata/test.csv")

X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
y = np.array([1, 2, 3, 4])



"""

This is for a specified train-testing split, we're doing kfold (more accurate for data that we don't know the integrity of, if confused, ask me :D)
train_X, test_X, train_y, test_y = train_test_split(trainData, trainSurvived, test_size=0.2, shuffle=False)

"""

kf = KFold(n_splits=2)#10)

for train_index, test_index in kf.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]