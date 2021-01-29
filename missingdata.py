import fileinput
global testDataDict
testDataDict = {}


testdata = open('testdata/test.csv', 'r')
x = 1
for i in testdata:
    if x == 1:
        pass
    else:
        line = i.split('\n')
        stringLine = str(line)
        if stringLine.count('"') == 2:
            print('There are two " in the string')
            pass
        else:
            index = 0
            for element in stringLine:
                if (element == '"' and stringLine[index - 1] == ',') or (element == '"' and stringLine[index + 1] == ','):
                    index+=1
                    pass
                else:
                    stringLine = stringLine[0:(index-1)] + stringLine [(index+1):len(stringLine)]
                    index+=1
        initSplit = str(line).split('"')
        name = initSplit[1]
        leftList = str(initSplit[0]).split(',')
        rightList = str(initSplit[2]).split(',')
        del rightList[0]
        print(rightList)
        passengerID = leftList[0]
        testDataDict[passengerID] = {}
        testDataDict[passengerID]['passengerID'] = leftList[0]
        testDataDict[passengerID]['class'] = leftList[1]
        testDataDict[passengerID]['name'] = name
        testDataDict[passengerID]['gender'] = rightList[0]
        testDataDict[passengerID]['age'] = rightList[1]
        testDataDict['siblingsspouses'] = rightList[2]
        testDataDict['parentschildren'] = rightList[3]
        testDataDict['ticketNo'] = rightList[4]
        testDataDict['fare'] = rightList[5]
        testDataDict['cabin'] = rightList[6]
        testDataDict['embarked'] = rightList[7]
    x+=1

"""for (key) in testDataDict:
    print(key, testDataDict[key])"""