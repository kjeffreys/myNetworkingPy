import numpy as np
import pyautogui as pawg
import pandas as pd
import time

# TODO: Make dict of locations based on res
# e.g. {values with left half of screen}
#      {values with full screen}

driverMap = {'2300': 1,
'dell': 2, 'm452': 3, 'm400':3,
'm401': 3,'m607': 4, 'm609': 4,
'm402': 5, 'm403': 5, 'm404': 6,
'm405': 6, 'm501': 7, 'hp': 8,
'5755':9}

class PrinterLoc():
    def __init__(self):
        self.x = 742
        self.y = 172

    def moveDown(self):
        self.y += 24

ppp = 18 # Printers Per Page
again = 'y'
'''
campAcctDict = {
    'Name': ['Nasser Borno', 'Owens Borno', 'Kimberly Garcia', 'Jaelle Gilles', 'Stephanie Gilles', 'Stephanie Lugo', 'Paul Mores', 'Maitry Sewnath', 'Cayla Thomas'],
    'Email': ['cp1@ercsd.org']
    #'GRADE': [6,9,7,7,8,7,8,4,1,1,1],
    #'ALREADY_EXISTED': ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO']
}
print(len(campAcctDict['Name']))
print(len(campAcctDict['Email']))
campAccts = pd.DataFrame( dict([ (k, pd.Series(v)) for k,v in campAcctDict.items() ]))
'''

def getPosition():
    return pawg.position()

def clickSearch(x=644, y=345):

    # click Manage Printer first to get search after first printer
    pawg.click(78, 537)
    time.sleep(2)

    pawg.click(x,y)

def clickPrinter(printerLoc): #first obj at 428,174, then moves down
    pawg.click(printerLoc.x, printerLoc.y)
    printerLoc.moveDown()

def clickOkay(x=417,y=409):
    pawg.click(x,y)

def clickDrivers(x=474,y=230):
    pawg.click(x,y)
    time.sleep(10)

def checkDrivers():
    clickDrivers()

    # Click dropdown list
    pawg.click(522,357)
    time.sleep(1)

    # Move to Win7 option for prev driver
    #pawg.drag(0,52)
    for i in range(4):
        pawg.press("down") # do X times to get to right select
    time.sleep(1)

    # Select Win7 drivers
    pawg.press("enter")
    #time.sleep(10)
    #pawg.click()

def pickWin10(pick):
    move = driverMap[pick]

    #Select [None]
    pawg.click(412,527)
    # move down until driver
    for i in range(move):
        pawg.press("down")


def setDrivers(driver):
    # Click dropdown list
    pawg.click(522,357)
    time.sleep(2)

    # Move to Win7 option for prev driver
    #pawg.drag(0,52)
    for i in range(6):
        pawg.press("down") # do X times to get to right select
    time.sleep(1)
    pawg.press("enter")

    # Select Win10 driver
    pickWin10(driver)
    print("Select: {}".format(driver))
    pawg.click(1015,685)
    wait = input("Enter to continue\n")
    
    # Click Apply
    pawg.click(586,655)
    time.sleep(6)
    # Click OK
    pawg.click(393, 656)
    #pawg.click()
    '''
    Somehow copy the text of the Driver
    after "Driver: "

    Then go to the dropdown (new position)

    Go to Win10 drivers

    Pick same if available 
    (probably manual verify, lot's of
    drivers missing)
    '''

def processPrinters():
    #for i in range(18):

    # Open search window for printers
    clickSearch()
    time.sleep(5)
            
    # Select the next printer
    clickPrinter(nextPrinter)
    time.sleep(2)

    # Confirm entry
    clickOkay()
    time.sleep(4)

    # Click Drivers tab
    checkDrivers()

    # Make vscode the active window for entering input easier
    print("Enter the Win7 driver found")
    pawg.click(1015, 685)
    driver = input("\n")

    setDrivers(driver)
    pawg.click(1015, 685)
    again = input("Enter 'y' to do next printer... ")
    if again == 'y' or again == 'yes':
        processPrinters()
    else:
        exit
    # Gives time to stop program if error
    # Otherwise iterates to next printer

'''
    again = input("Get next printer?")      
    
    if again == 'y':
        processPrinters()
        print("opening next printer object")
    '''

if __name__ == "__main__":
    nextPrinter = PrinterLoc()
    processPrinters()