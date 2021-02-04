import csv
global myList
global myDict
myList = []
myDict = {}

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
    passengerID = myList[i][0]
    myDict[passengerID] = {}
    myDict[passengerID]['passengerID'] = myList[i][0]
    myDict[passengerID]['class'] = myList[i][1]
    myDict[passengerID]['name'] = myList[i][2]
    myDict[passengerID]['gender'] = myList[i][3]
    myDict[passengerID]['age'] = myList[i][4]
    myDict[passengerID]['siblings/spouses'] = myList[i][5]
    myDict[passengerID]['parents/children'] = myList[i][6]
    myDict[passengerID]['ticketNo'] = myList[i][7]
    myDict[passengerID]['fare'] = myList[i][8]
    myDict[passengerID]['cabin'] = myList[i][9]
    myDict[passengerID]['embarked'] = myList[i][10]
    print(myDict[passengerID])

for i in range(len(myList)):
    passengerID = myList[i][0]
    for x in range(len(myList[i])):
        if (myList[i][x] == '' or myList[i][x] == ' ') and (myList[i][0] != 'incomplete'):
            myList[i].insert(0, 'incomplete')
            break
        
        elif (myList[i][0] != 'complete' and myList[i][0] != 'incomplete' and x == 10):
            myList[i].insert(0, 'complete')
        else:
            pass

for i in range(len(myList)):
    passengerID = myList[i][0]
    print(myList[i])
    print(myDict[passengerID])
