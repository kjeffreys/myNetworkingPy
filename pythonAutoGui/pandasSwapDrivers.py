import numpy as np
import pyautogui as pg
import pandas as pd
import os
import time

manageX1 = 74
manageY1 = 517
searchBtnX1 = 580
searchBtnY1 = 348
searchTabX1 = 562
searchTabY1 = 121
searchBarX1 = 458
searchBarY1 = 236
queryObjX1 = 720
queryObjY1 = 187
clickSelectOkayX1 = 374
clickSelectOkayY1 = 389
driversTabX1 = 433
driversTabY1 = 245
osDropDownX1 = 473
osDropDownY1 = 358
setVsCodeActiveX1 = 1043
setVsCodeActiveY1 = 650
clickEnterSearchX1 = 540
clickEnterSearchY1 = 384

filePath = os.path.join("C:\\","Users", "kjeffreys",
"Desktop", "PomPrinters.xlsx")

driverMap = {'2330': 1,
'dell': 2, 'm452': 3, 'm400':3,
'm401': 3,'m607': 4, 'm609': 4,
'm402': 5, 'm403': 5, 'm404': 6,
'm405': 6, 'm501': 7, 'hp': 8,
'5755':9}

printers = pd.read_excel(filePath)

def iteratePrinters(currentRow):
    return str(currentRow) + "*"

def clickOkay(x=clickSelectOkayX1,y=clickSelectOkayY1):
    pg.click(x,y)
    time.sleep(2.5)

def setDrivers():
    pg.click(driversTabX1,driversTabY1)
    time.sleep(7)
    pg.click(osDropDownX1, osDropDownY1)
    time.sleep(.5)
    # Move down to Win10 options
    for i in range(6):
        pg.press("down")
    time.sleep(.5)
    pg.press("enter")
    time.sleep(10)
    pg.click(setVsCodeActiveX1,setVsCodeActiveY1)
    wait = input("Press enter to continue:\n")
    

def processPrinters():
    for i in range(45):
        obj = iteratePrinters(str(printers.iloc[i]['Room']))
        pg.click(manageX1,manageY1)
        time.sleep(1)
        pg.click(searchBtnX1,searchBtnY1)
        time.sleep(3)
        pg.click(searchTabX1,searchTabY1)
        time.sleep(1)
        pg.click(searchBarX1, searchBarY1)
        pg.write(obj)
        pg.press("enter")
        time.sleep(3)
        pg.click(queryObjX1,queryObjY1)
        time.sleep(2)
        clickOkay()
        setDrivers()

    again = input("continue?\n")
    if again == 'y' or again == 'yes':
        print("Next printer...\n")
    else:
        exit

if __name__ == "__main__":
    #print(printers.info())
    #print(printers.describe())
    #print(printers.index)
    processPrinters()    
