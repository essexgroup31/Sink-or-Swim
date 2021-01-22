import csv

def csv_read(filename):
    peopleList = []

    myFile = open("Test Data/" + filename, mode = "r")

    reader = csv.reader(myFile)

    for each in reader:
        peopleList.append(each)

    myFile.close()

    return(peopleList)
