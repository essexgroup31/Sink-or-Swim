import pandas as pd

def csv_read(filename):
    csvFile = pd.read_csv("Test Data/" + filename)

    return(csvFile)
