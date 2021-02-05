import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree






train_data = pd.read_csv("Test Data/train.csv")
test_data = pd.read_csv("Test Data/test.csv")

features = ["Pclass", "Sex", "SibSp", "Parch"]

X = pd.get_dummies(train_data[features])

X_test = pd.get_dummies(test_data[features])

y = train_data["Survived"]


clf = tree.DecisionTreeClassifier()#n_estimators = 1300)

clf.fit(X,y)

survived = clf.predict(X_test)

submission = pd.DataFrame({"PassengerId": test_data["PassengerId"], "Survived": survived})

submission.to_csv("Test Data/submission.csv", index = False)

print("File submission.csv, has been created")

