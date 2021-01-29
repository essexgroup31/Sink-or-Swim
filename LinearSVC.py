import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm

train_data = pd.read_csv("Test Data/train.csv") # train_data is the data we're training our ML algo on
test_data = pd.read_csv("Test Data/test.csv")   # test_data is the data we're testing our ML algo on

features = ["Pclass", "Sex", "SibSp", "Parch"] # The attributes we want currently
# I've removed some of the attributes because they aren't complete in the csv files. (TODO)

X = pd.get_dummies(train_data[features])
# Basically for sex, there are two things
# Male and Female, so the get_dummies basically just
# sets the data to categories, which will make it easier
# for the ML algo.

X_test = pd.get_dummies(test_data[features])


# So the way the ML algorithm works is we fit a set of data to a set of outcomes
# We have the set of data (train_data), so we need a set of outcomes, which is already in train_data.
# and it's the survived column
y = train_data["Survived"]


# So linearSVC is the ML algorithm we're now using
# We need more iterations (causes warnings if it's too low)
clf = svm.LinearSVC(max_iter= 10000)

# We fit the training data to it's outcomes
clf.fit(X,y)

# And then we predict the test data.
survived = clf.predict(X_test)

# We then need to somehow output the file
# I did this by creating a DataFrame (basically a bit like an excel sprdsht)
# It has two columns, PassengerId, and Survived
submission = pd.DataFrame({"PassengerId": test_data["PassengerId"], "Survived": survived})

# Send to csv without indexes (idk why you'd ever need indexes.)
submission.to_csv("Test Data/submission.csv", index = False)

print("File submission.csv, has been created")

w = clf.coef_[0] # The coefficients of the algo, might need to look at later