import pandas as pd

# MAKE SURE YOU READ
# So, i've cleaned everything up, and this will (hopefully) serve as an example of how to use everything in conjunction 

from fixdata import fixData

# fixdata is a python file (you can probably guess what it does)
# within fixdata, there is a function called fixData()
# 
# def fixData(trainFileName, testFileName, imputer = "simple", strategy = "mean")
#
# The fixdata function, takes the filepath of both test and train csv files.
# The imputer is the method of fixing the data, options are: "simple", "knn" and "iterative"
# The strategy only applies to the "simple" and "iterative" methods, and the options are: "mean", "most_frequent", "median" and "constant"
# The inputs are defaulted to simple imputer with a mean strategy
#
# return(dummied_test, dummied_train, trainSurvived, passengerID)
#
# The function will return:
# dummied_test is the testing file with dummies (if you ask, i'll explain) it'll work as the testing data
# dummied_train is the training file with dummies (if you ask, i'll explain) it'll work as the training data
# trainSurvived is the list of 1's and 0's of people who survived, it is needed for training the machine learning algorithm
# passengerID is the list of passenger's ID, it is needed for the final submission file


testData, trainData, trainSurvived, passengerID = fixData("testdata/train.csv", "testdata/test.csv")

# Set the returned variables of the function

from mlAlgos import *

# mlAlgos is a python file which contains all of the machine learning algorithms
# that i've coded, all of the functions take:
# trainData, testData, trainSurvived, passengerID (all of these are already explained above)
# each of the algorithms all return a pandas dataframe, which is basically like a
# excel spreadsheet which contains a column of the passenger's IDs and what our algorithm predicted about their survival

#submission = LinearSVC(trainData, testData, trainSurvived, passengerID)
submission = SVC(trainData, testData, trainSurvived, passengerID)

# To then send this to a file, you can do
# variablename.to_csv(filepath to send to)
# set the index to false, otherwise an index is in the file, which kaggle doesn't want.

submission.to_csv("testdata/submission.csv", index=False)