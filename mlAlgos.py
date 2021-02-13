import pandas as pd
from sklearn import svm
from sklearn import tree
from sklearn.linear_model import LogisticRegression

def LinearSVC(trainData, testData, trainSurvived, passengerID):

    clf = svm.LinearSVC(max_iter=100000)

    clf.fit(trainData, trainSurvived)

    survived = clf.predict(testData)

    submission = pd.DataFrame({"PassengerId": passengerID, "Survived": survived})

    return(submission)

def LogisticRegression(trainData, testData, trainSurvived, passengerID):

    clf = LogisticRegression()

    clf.fit(trainData, trainSurvived)

    survived = clf.predict(testData)

    submission = pd.DataFrame({"PassengerId": passengerID, "Survived": survived})

    return(submission)

def RandomForest(trainData, testData, trainSurvived, passengerID):

    clf = tree.DecisionTreeClassifier()#n_estimators = 1300)

    clf.fit(trainData, trainSurvived)

    survived = clf.predict(testData)

    submission = pd.DataFrame({"PassengerId": passengerID, "Survived": survived})

    return(submission)

def SVC(trainData, testData, trainSurvived, passengerID):

    clf = svm.SVC(kernel="linear")

    clf.fit(trainData, trainSurvived)

    survived = clf.predict(testData)

    submission = pd.DataFrame({"PassengerId": passengerID, "Survived": survived})

    return(submission)