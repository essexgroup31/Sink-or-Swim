import pandas as pd
from sklearn import svm
from sklearn import tree
from sklearn.linear_model import LogisticRegression

features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
#old_features = ["Pclass", "Sex", "SibSp", "Parch"]

def LinearSVC(train_data, test_data):

    X = pd.get_dummies(train_data[features])

    X_test = pd.get_dummies(test_data)

    y = train_data["Survived"]

    clf = svm.LinearSVC(max_iter=10000)

    clf.fit(X,y)

    survived = clf.predict(X_test)

    submission = pd.DataFrame({"PassengerId": test_data["PassengerId"], "Survived": survived})

    return(submission)

def LogisticRegression(train_data, test_data):

    X = pd.get_dummies(train_data[features])

    X_test = pd.get_dummies(test_data)

    y = train_data["Survived"]

    clf = LogisticRegression()

    clf.fit(X,y)

    survived = clf.predict(X_test)

    submission = pd.DataFrame({"PassengerId": test_data["PassengerId"], "Survived": survived})

    return(submission)

def RandomForest(train_data, test_data):

    X = pd.get_dummies(train_data[features])

    X_test = pd.get_dummies(test_data)

    y = train_data["Survived"]

    clf = tree.DecisionTreeClassifier()#n_estimators = 1300)

    clf.fit(X,y)

    survived = clf.predict(X_test)

    submission = pd.DataFrame({"PassengerId": test_data["PassengerId"], "Survived": survived})

    return(submission)

def SVC(train_data, test_data):

    X = pd.get_dummies(train_data[features])

    X_test = pd.get_dummies(test_data)

    y = train_data["Survived"]

    clf = svm.SVC(kernel="linear")

    clf.fit(X,y)

    survived = clf.predict(X, y)

    submission = pd.DataFrame({"PassengerId": test_data["PassengerId"], "Survived": survived})

    return(submission)



