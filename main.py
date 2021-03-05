import sys, os, time
import pandas as pd
from itertools import chain, combinations

from fixdata import fixData
from mlAlgos import *
from interface import *

## Current TODO List:
# - Move Model caller to a function
# - Make dummies non-required. Currently required. Check fixData.py for more info
# - Make algorithm only test multiple CVs if it looks promising. This can be done by putting a lower CV value into the Cross Validation function, and re-calling itself if the mean result is near the upper third of the highest result

models = [SVC, randomForest] ## Available models are SVC, LinearSVC, Logistic Regression and Random Forest
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

## -- MESS WITH STUFF ABOVE THIS LINE ONLY -------------------------------------------

os.system("clear")

def powerset(iterable):
    s = list(set(iterable))
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

featuresPowerset = []

for i, combo in enumerate(powerset(features), 1):
    featuresPowerset.append(combo)

topFeatureSet = [0, 0, models[0], "features"]

print("The highest current Simulated Average is", topFeatureSet[0], "with a standard deviation of", topFeatureSet[1], "using the", topFeatureSet[2].__name__, "model and the features", topFeatureSet[3], "\n\n")

for i in range(len(featuresPowerset)):
    if len(featuresPowerset[i]) < 3:
        pass
    elif ('Sex' not in featuresPowerset[i]) or ('Embarked' not in featuresPowerset[i]):
        pass
    else:
        currentFeatures = featuresPowerset[i]

        print("-- Now predicting using", currentFeatures, "-------------\n")
        testData, trainData, trainSurvived, passengerID = fixData("Training Data/train.csv", "Test Data/test.csv", currentFeatures)

        for i in (range(len(models))):
            model = models[i]
            returnPath = "Returns/submission" + str(model.__name__) + ".csv"
            submission, scores = model(trainData, testData, trainSurvived, passengerID)
            submission.to_csv(returnPath, index=False)
            print((model.__name__), "model produces accuracy of %0.3f with a standard deviation of %0.2f" % (scores.mean(), scores.std()),"\n")
            if (scores.mean() > topFeatureSet[0]):
                topFeatureSet[0] = round(scores.mean(), 3)
                topFeatureSet[1] = round(scores.std(), 2)
                topFeatureSet[2] = model
                topFeatureSet[3] = currentFeatures
        os.system("clear")
        print("The highest current Simulated Average is", topFeatureSet[0], "with a standard deviation of", topFeatureSet[1], "using the", topFeatureSet[2].__name__, "model and the features", topFeatureSet[3], "\n\n")


os.system("clear")
print("The highest Simulated Average was", topFeatureSet[0], "with a standard deviation of", topFeatureSet[1], "using the", topFeatureSet[2].__name__, "model and the features", topFeatureSet[3], "\n\n")

model = topFeatureSet[2] ##This can be converted into a function TODO
testData, trainData, trainSurvived, passengerID = fixData("Training Data/train.csv", "Test Data/test.csv", topFeatureSet[3])
returnPath = "./Returns/submissionBest.csv"
submission, scores = model(trainData, testData, trainSurvived, passengerID)
submission.to_csv(returnPath, index=False)
print("\nFinal submission created at", returnPath,"\n\n")
