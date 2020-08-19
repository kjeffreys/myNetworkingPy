import numpy as np
import pyautogui as pg
import pandas as pd
import os
import time

manageX1 = 78
manageY1 = 489
searchBtnX1 = 580
searchBtnY1 = 321
driversTabX1 = 432
driversTabY1 = 216
searchTabX1 = 562
searchTabY1 = 121
searchBarX1 = 458
searchBarY1 = 236
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
    str(printers.iloc[i]) + "*"

def processPrinters():
    for i in range(45):
        obj = iteratePrinters(str(printers.iloc[i]) + "*")
        pg.click(manageX1,manageY1)
        pg.click(searchBtnX1,searchBtnX2)
        pg.click(searchTabX1,searchTabY1)
        pg.click(searchBarX1, searchBarY1)
        pg.enter(obj)
        pg.click()
        # click Okay

if __name__ == "__main__":
    #print(printers.info())
    #print(printers.describe())
    #print(printers.index)
    
