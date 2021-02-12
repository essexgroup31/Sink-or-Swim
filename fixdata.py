from sklearn import impute
import numpy as np
import pandas as pd

def fixData(trainFileName, testFileName, imputer = "simple", strategy = "mean"):

    training_data = pd.read_csv(trainFileName)
    testing_data = pd.read_csv(testFileName)

    neededFeatures = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
    featuresForDummies = ["Embarked", "Sex"]

    testSurvived = training_data["Survived"]
    passengerID = testing_data["PassengerId"]

    training_data = training_data[neededFeatures]
    testing_data = testing_data[neededFeatures]

    tr_data = pd.get_dummies(training_data, columns=featuresForDummies)
    te_data = pd.get_dummies(testing_data, columns=featuresForDummies)

    if imputer.lower() == "simple":
        imp = impute.SimpleImputer(missing_values = np.NaN, strategy = strategy)
    elif imputer.lower() == "knn":
        imp = impute.KNNImputer(missing_values = np.NaN)
    elif imputer.lower() == "iterative":
        imp = impute.IterativeImputer(missing_values = np.NaN, initial_strategy = strategy)
    else:
        print("You did not enter a correct imputation method.")
        print("Correct imputation methods include: \"Simple\", \"KNN\", \"Iterative\"")
    

    imp.fit(te_data)
    dummied_test = imp.transform(te_data)

    imp.fit(tr_data)
    dummied_train = imp.transform(tr_data)

    print("Data fixed.")

    return(dummied_test, dummied_train, testSurvived, passengerID)