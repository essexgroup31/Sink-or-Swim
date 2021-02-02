import csv
global myList
myList = []
def read_csv(filename):

    myFile = open(filename, "r")

    global myList
    myList = []

    x = csv.reader(myFile)
    
    for each in x:
        myList.append(each)

    myFile.close()

    myList.pop(0)

    return(myList)

read_csv('testdata/test.csv')
for i in range(len(myList)):
    print(myList[i])
