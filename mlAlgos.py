import pandas as pd
from sklearn import svm
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import inspect

#These all take the inputs required, train a model, then test against that model, and then use cross validation to test how accurate they are

def linearSVC(trainData, testData, trainSurvived, passengerID):
    
    print("Predicting Data using LinearSVC")
    clf = 0
    clf = svm.LinearSVC(max_iter=10000000, C=0.2)
    clf.fit(trainData, trainSurvived)
    survived = clf.predict(testData)
    submission = pd.DataFrame({"PassengerId": passengerID, "Survived": survived})

    simAcc = simulateAccuracy(clf, trainData, trainSurvived, cv=3)
    
    return (submission), simAcc


def logisticRegression(trainData, testData, trainSurvived, passengerID):

    print("Predicting Data using Logistic Regression")
    clf = LogisticRegression()
    clf.fit(trainData, trainSurvived)
    survived = clf.predict(testData)
    submission = pd.DataFrame({"PassengerId": passengerID, "Survived": survived})

    simAcc = simulateAccuracy(clf, trainData, trainSurvived, cv=5)

    return (submission), simAcc


def randomForest(trainData, testData, trainSurvived, passengerID):

    print("Predicting Data using Random Forest")
    clf = tree.DecisionTreeClassifier()  # n_estimators = 1300)
    clf.fit(trainData, trainSurvived)
    survived = clf.predict(testData)
    submission = pd.DataFrame({"PassengerId": passengerID, "Survived": survived})

    simAcc = simulateAccuracy(clf, trainData, trainSurvived, cv=5)

    return (submission), simAcc


def SVC(trainData, testData, trainSurvived, passengerID):
    
    print("Predicting Data using SVC")
    clf = 0
    clf = svm.SVC() #TODO Perhaps the kernel shouldn't be linear?
    clf.fit(trainData, trainSurvived)
    survived = clf.predict(testData)
    submission = pd.DataFrame({"PassengerId": passengerID, "Survived": survived})

    simAcc = simulateAccuracy(clf, trainData, trainSurvived, cv=5)

    return (submission), simAcc

def simulateAccuracy(clf, trainData, trainSurvived, cv):
    print("Simulating Accuracy for", (inspect.stack()[1].function))
    scores = cross_val_score(clf, trainData, trainSurvived, cv=cv)
    return scores