from sklearn import impute
import numpy as np
import pandas as pd

def fixData(trainFileName, testFileName, features, imputer = "simple", strategy = "mean"):

    print("Fixing Data\n") #Read files into pandas array
    training_data = pd.read_csv(trainFileName)
    testing_data = pd.read_csv(testFileName)

    featuresForDummies = ["Embarked", "Sex"]

    trainSurvived = training_data["Survived"] 
    passengerID = testing_data["PassengerId"]

    features2 = []
    for i in range(len(features)):
        features2.append(features[i]) #Appends feature selected to the features to use

    training_data = training_data[features2]
    testing_data = testing_data[features2]

    tr_data = pd.get_dummies(training_data, columns=featuresForDummies) #Get dummies for required ones
    te_data = pd.get_dummies(testing_data, columns=featuresForDummies)

    if imputer.lower() == "simple":
        imp = impute.SimpleImputer(missing_values = np.NaN, strategy = strategy) #Imputes data
    elif imputer.lower() == "knn":
        imp = impute.KNNImputer(missing_values = np.NaN)
    elif imputer.lower() == "iterative":
        imp = impute.IterativeImputer(missing_values = np.NaN, initial_strategy = strategy)
    else:
        print("You did not enter a correct imputation method.")
        print("Correct imputation methods include: \"Simple\", \"KNN\", \"Iterative\"")
    

    imp.fit(te_data)
    dummied_test = imp.transform(te_data) #Fits data

    imp.fit(tr_data)
    dummied_train = imp.transform(tr_data)

    return(dummied_test, dummied_train, trainSurvived, passengerID) #Returns the completed arrays