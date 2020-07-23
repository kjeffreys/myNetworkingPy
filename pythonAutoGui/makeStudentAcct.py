import numpy as np
import pyautogui as pawg
import pandas as pd
import time

# TODO: Make dict of locations based on res
# e.g. {values with left half of screen}
#      {values with full screen}
studentDict = {
    'STUDENT': ['Avrohom Goldberg', 'Abraham Holtzer', 'Nehuma Chumie Schnitzler', 'Chaya Leitman', 'Chava Bracha Klugman', 'Faigy Ausch', 'Yahir Mazariego', 'Ali Grant', 'Louis Gross', 'Katherinez Gome-Hernandez', 'Christian Vilela-Suriano'],
    'ID': ['880846', '808193', '809670', '810706', '808746', '875416', '879688', '887685', '896622', '905457', '906214'],
    'GRADE': [6,9,7,7,8,7,8,4,1,1,1],
    'ALREADY_EXISTED': ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO']
}
print(len(studentDict['STUDENT']))
print(len(studentDict['ID']))
print(len(studentDict['GRADE']))
students = pd.DataFrame(studentDict)


def getPosition():
    return pawg.position()

def usernameClick(x=397, y=249):
    pawg.click(x, y)

def fnameClick(x=409, y=276):
    pawg.click(x, y)
    
def lnameClick(x=394, y=305):
    pawg.click(x, y)

def passwordClick():
    pawg.click(x, y)

def retypepasswordClick():
    pawg.click(x, y)

def templatecheckboxClick():
    pawg.click(x, y)

def isPrimary():
    # get user's full name from obj
    name = obj['STUDENT'].split()
    lunchId = obj['ID']
    grade = obj['GRADE']
    # get fname
    fname = name[0]
    # get lname
    lname = name[1:]
    print(lname)
    print(len(lname))
    # create username
    print(fname[0])
    print(lname[0])
    print(lname[0][0])
    print(lunchId)
    uname = fname[0] + lname[0][0] + lunchId

    # insert username
    usernameClick()
    pawg.write(uname)

    time.sleep(.5)

    # insert fname
    fnameClick()
    pawg.write(fname)

    time.sleep(.5)
    
    # insert lname
    lnameClick()
    pawg.write(("").join(lname))

    time.sleep(.5)

    # insert Context
    pawg.click(396,357)
    contextStr = getContext(grade)
    pawg.write(contextStr)

    time.sleep(.5)

    # insert pw: (391, 396)
    pawg.click(391, 396)
    pawg.write('1')

    time.sleep('1')

    # click retype: (395, 423)
    pawg.click(395, 423)
    pawg.write(lunchId)

    time.sleep(.5)

    # templ Checkbox (264, 560)
    pawg.click(264, 560)
    # templ TextBox(411, 587)
    pawg.click(411, 587)
    template = getTemplate(grade)


def notPrimary(obj):
    # get user's full name from obj
    name = obj['STUDENT'].split()
    lunchId = obj['ID']
    grade = obj['GRADE']
    # get fname
    fname = name[0]
    # get lname
    lname = name[1:]
    print(lname)
    print(len(lname))
    # create username
    print(fname[0])
    print(lname[0])
    print(lname[0][0])
    print(lunchId)
    uname = fname[0] + lname[0][0] + lunchId

    # insert username
    usernameClick()
    pawg.write(uname)

    time.sleep(.5)

    # insert fname
    fnameClick()
    pawg.write(fname)

    time.sleep(.5)
    
    # insert lname
    lnameClick()
    pawg.write(("").join(lname))

    time.sleep(.5)

    # insert Context
    pawg.click(396,357)
    contextStr = getContext(grade)
    pawg.write(contextStr)

    time.sleep(.5)

    # insert pw: (391, 396)
    pawg.click(391, 396)
    pawg.write(lunchId)

    time.sleep(.5)

    # click retype: (395, 423)
    pawg.click(395, 423)
    pawg.write(lunchId)

    time.sleep(.5)

    # templ Checkbox (264, 560)
    pawg.click(264, 560)
    # templ TextBox(411, 587)
    pawg.click(411, 587)
    template = getTemplate(grade)
    time.sleep(5)


    
def getGradeCode(grade):
    gradeDict = {
        'K': '32',
        '1': '31',
        '2': '30',
        '3': '29',
        '4': '28',
        '5': '27',
        '6': '26',
        '7': '25',
        '8': '24',
        '9': '23' # 2 HS and ambiguous as to where students are. impl elsewhere
    }
    return gradeDict[str(grade)]

def getContext(grade):
    gC = getGradeCode(grade)
    contextDict = {
        '32': '32.Primary.Students.eUsers.ERCSD',
        '31': '31.Primary.Students.eUsers.ERCSD',
        '30': '30.Primary.Students.eUsers.ERCSD',
        '29': '29.Primary.Students.eUsers.ERCSD',
        '28': '28.Intermediate.Students.eUsers.ERCSD',
        '27': '27.Intermediate.Students.eUsers.ERCSD',
        '26': '26.Intermediate.Students.eUsers.ERCSD',
        '25': '25.MiddleSchools.Students.eUsers.ERCSD',
        '24': '24.MiddleSchools.Students.eUsers.ERCSD',
        '23': '23.RHS.Students.eUsers.ERCSD', #HS is ambiguous, separate out
        #'SVHS9': 'SVHS.Students.eUsers.ERCSD' to protect this function
    }

    return contextDict[gC]

def getTemplate(grade):
    '''
    gC = getGradeCode(grade)
    templateDict = {
        '32': 'User_Template.32.Primary.Students.eUsers.ERCSD',

        '23': 'User_Template.23.RHS.Students.eUsers.ERCSD'
    }
    '''
    # B/c template autofills another field, it is not ideal to enter the text
    # But the selection of objects is off screen, so instead, implementing click and drag selection
    # of objects needed

    # position of hz scroll bar (407, 718)
    pawg.moveTo(407,718)
    # drag screen to see search button
    pawg.drag(100, 0, .5)
    # click search button (590, 585)
    pawg.click(590, 585)
    print("Done for now")


def processRows(df=students):
    for entry in df.index:
        print("process {}".format(entry))
        obj = df.iloc[entry]
        if obj['ALREADY_EXISTED'] == 'NO':
            if obj['GRADE'] > 3:
                notPrimary(obj)
            elif obj['GRADE'] <= 3:
                isPrimary(obj)
            else:
                print("obj not in grade range:\n{}".format(obj))
        pawg.click(936,15)
        pawg.click(66,456)
        #create user (66,456)
        #close search window(936, 15)    

def processSingleRow(df=students, rowNum=0):
    obj = df.iloc[rowNum]
    if obj['ALREADY_EXISTED'] == 'NO':
        if obj['GRADE'] > 3:
            notPrimary(obj)
        elif obj['GRADE'] <= 3:
            isPrimary(obj)
        else:
            print("obj not in grade range:\n{}".format(obj))
    
    return 0

def teacherIsNull(teacher):
    # "Search" tab (546,77)
    pawg.click(546,77)
    # Search field (432, 205)
    pawg.click(432,205)
    pawg.write(teacher)
    # Search button (529, 416)
    pawg.click(529, 416)
    resp = input()
    return resp
    
# Enter teacher list in here
def checkTeachers():
    teachers = ['bbarrow', 'nborno', 'oborno', 'sestevez', 'kgarcia', 'jgilles', 'sgilles', 'scelestin', 'mhenriquez', 'jhernandez', 'lkilkenny', 'glabaze', 'clouise', 'slugo', 'smcdonald', 'cmendez', 'mmend', 'pmores', 'cnorman', 'msewnath', 'jsimpson', 'cthomas']
    teachFrame = pd.DataFrame(columns=[teachers, 'Exists?'])
    for t in teachers:
        teacherIsNull(t)
        #time.sleep(3)

    print(teachFrame)
if __name__ == "__main__":
    #print(getPosition())
    #processRows()
    #processSingleRow(rowNum=0)
    '''for entry in students.index:
        print(entry)
    '''
    checkTeachers()