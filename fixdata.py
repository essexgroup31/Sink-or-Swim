from sklearn import impute
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

training_data = pd.read_csv("testdata/train.csv")

testing_data = pd.read_csv("testdata/test.csv")

features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
features2 = ["Embarked", "Sex"]

y = training_data["Survived"]
passengerID = testing_data["PassengerId"]

training_data = training_data[features]
testing_data = testing_data[features]

tr_data = pd.get_dummies(training_data, columns=features2)
te_data = pd.get_dummies(testing_data, columns=features2)


imp = impute.SimpleImputer(missing_values=np.NaN, strategy = "median")
# Mean median most_frequent constant

imp.fit(te_data)
dummied_test = imp.transform(te_data)

imp.fit(tr_data)
dummied_train = imp.transform(tr_data)


clf = LogisticRegression(max_iter = 1000)

clf.fit(dummied_train, y)

survived = clf.predict(dummied_test)

submission = pd.DataFrame({"PassengerId": passengerID, "Survived": survived})

submission.to_csv("testdata/submission.csv", index = False)
print("DONE! IDIOTS")
