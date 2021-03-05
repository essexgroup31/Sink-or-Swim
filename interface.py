import os, sys, time


def getData():
    clearScreen()
    dataInFolder = False
    while dataInFolder == False:
        if not os.listdir("./Training Data/"):
            waitForEnter = input(
                "No training data found! Please put your training data in the /Training Data directory, and then press enter to continue.")
        else:
            useFolderData = input("\nI see you've got data in the Training Data Folder, do you want to use that?\n")
            if useFolderData == "yes" or "y" or "Yes" or "Y":
                print("Great! Lets get to work")
                dataInFolder = True
                pass

def clearScreen():
    os.system("clear")

def notifyDialog(title, text):
    os.system("""
              osascript -e 'display dialog "{}" with title "{}"'
              """.format(text, title))