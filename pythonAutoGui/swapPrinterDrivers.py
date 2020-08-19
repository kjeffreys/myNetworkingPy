import numpy as np
import pyautogui as pawg
import pandas as pd
import time

# TODO: Make dict of locations based on res
# e.g. {values with left half of screen}
#      {values with full screen}

managePrinterX1 = 78
managePrinterY1 = 489
searchBtnX1 = 580
searchBtnY1 = 321
driversTabX1 = 432
driversTabY1 = 216

driverMap = {'2330': 1,
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
        self.y += 21

class PrinterLoc2():
    def __init__(self):
        self.x = 736
        self.y = 205

    def moveDown(self):
        self.y += 21

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

def clickSearch():

    # click Manage Printer first to get search after first printer
    pawg.click(managePrinterX1,managePrinterY1)
    time.sleep(2)

    pawg.click(searchBtnX1,searchBtnY1)
    time.sleep(3)

def clickPage2():
    # click Manage Printer first to get search after first printer
    pawg.click(managePrinterX1, managePrinterY1)
    time.sleep(3)

    pawg.click(searchBtnX1,searchBtnY1)
    time.sleep(3)
    #NOTE: Now adding next page click
    pawg.click(818,590)
    time.sleep(2)

def clickPrinter(printerLoc2): #first obj at 428,174, then moves down
    pawg.click(printerLoc2.x, printerLoc2.y)
    printerLoc2.moveDown()

def clickOkay(x=417,y=409):
    pawg.click(x,y)

def clickOkay2(x=373, y=362):
    pawg.click(x,y)
    time.sleep(1)

def clickDrivers(x=474,y=230):
    pawg.click(x,y)
    time.sleep(10)

def clickDrivers2():
    pawg.click(driversTabX1,driversTabY1)
    time.sleep(7)

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

def verifyDrivers():
    clickDrivers2()

    # Click dropdown list
    #pawg.click(522,357)
    pawg.click(474,331)
    time.sleep(1)

    # Move to Win7 option for prev driver
    #pawg.drag(0,52)
    for i in range(6):
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

def verifyPrinters():
    #for i in range(18):

    # Open search window for printers
    clickSearch()
    time.sleep(5)
            
    # Select the next printer
    clickPrinter(nextPrinter2)
    time.sleep(2)

    # Confirm entry
    clickOkay()
    time.sleep(4)

    # Click Drivers tab
    verifyDrivers()

    '''
    # Make vscode the active window for entering input easier
    print("Enter the Win7 driver found")
    pawg.click(1015, 685)
    driver = input("\n")
    
    setDrivers(driver)
    '''
    pawg.click(1015, 685)
    again = input("Enter 'y' to do next printer... ")
    if again == 'y' or again == 'yes':
        verifyPage2()
    else:
        exit
    # Gives time to stop program if error
    # Otherwise iterates to next printer

def verifyPage1():
    #for i in range(18):

    # Open search window for printers
    clickSearch()
    time.sleep(2)
            
    # Select the next printer
    clickPrinter(nextPrinter2)
    time.sleep(2)

    # Confirm entry
    clickOkay2()
    time.sleep(4)

    # Click Drivers tab
    verifyDrivers()

    '''
    # Make vscode the active window for entering input easier
    print("Enter the Win7 driver found")
    pawg.click(1015, 685)
    driver = input("\n")
    
    setDrivers(driver)
    '''
    pawg.click(1015, 685)
    again = input("Enter 'y' to do next printer... ")
    if again == 'y' or again == 'yes':
        verifyPage1()
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


def verifyPage2():
    #for i in range(18):

    # Open search window for printers
    clickPage2()
    time.sleep(2)
            
    # Select the next printer
    clickPrinter(nextPrinter2)
    time.sleep(2)

    # Confirm entry
    clickOkay2()
    time.sleep(4)

    # Click Drivers tab
    verifyDrivers()

    '''
    # Make vscode the active window for entering input easier
    print("Enter the Win7 driver found")
    pawg.click(1015, 685)
    driver = input("\n")
    
    setDrivers(driver)
    '''
    pawg.click(1015, 685)
    again = input("Enter 'y' to do next printer... ")
    if again == 'y' or again == 'yes':
        verifyPage2()
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
    #nextPrinter = PrinterLoc()
    nextPrinter2 = PrinterLoc2()
    #verifyPage1()
    verifyPage2()
    #verifyPage3()