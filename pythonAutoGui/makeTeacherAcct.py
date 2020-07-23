import numpy as np
import pyautogui as pawg
import pandas as pd
import time

# TODO: Make dict of locations based on res
# e.g. {values with left half of screen}
#      {values with full screen}
campAcctDict = {
    'Name': ['Nasser Borno', 'Owens Borno', 'Kimberly Garcia', 'Jaelle Gilles', 'Stephanie Gilles', 'Stephanie Lugo', 'Paul Mores', 'Maitry Sewnath', 'Cayla Thomas'],
    'Email': ['cp1@ercsd.org']
    #'GRADE': [6,9,7,7,8,7,8,4,1,1,1],
    #'ALREADY_EXISTED': ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO']
}
print(len(campAcctDict['Name']))
print(len(campAcctDict['Email']))
campAccts = pd.DataFrame( dict([ (k, pd.Series(v)) for k,v in campAcctDict.items() ]))


def getPosition():
    return pawg.position()

def usernameClick(x=397, y=249):
    pawg.click(x, y)

def fnameClick(x=409, y=276):
    pawg.click(x, y)
    
def lnameClick(x=394, y=305):
    pawg.click(x, y)

def passwordClick(x=0, y=0):
    pawg.click(x, y)

def retypepasswordClick(x=0, y=0):
    pawg.click(x, y)

def templatecheckboxClick():
    pawg.click(x, y)

def getFname(name):
    return name[0]

def getLname(name):
    return " ".join(name[1:])

def getUsername(fname, lname, acctsMade):
    return 'cp' + str(acctsMade + 3)

def getTemplate():
    # Click "Template" filter
    pawg.click(447, 303)
    time.sleep(1) # for testing
    # Click "Apply" filter
    pawg.click(525, 399)
    time.sleep(2) # keep this sleep, it involves loading backend data
    # Select template
    pawg.click(750, 155)
    time.sleep(2) # for testing

def makeAcct(obj, acctsMade):
    # setup fields from user + increment of acctsMade
    name = obj['Name'].split()
    fname = getFname(name)
    lname = getLname(name)
    username = getUsername(fname, lname, acctsMade)
    
    insertUsername(username)
    insertFname(fname)
    insertLname(lname)
    insertContext()
    insertPassword()
    insertPwVerify()

    insertTemplate()
    insertEmail(username)

def insertUsername(uname):
    # insert username
    usernameClick()
    pawg.write(uname)

def insertFname(fname):
    # insert fname
    fnameClick()
    pawg.write(fname)

def insertLname(lname):
    # insert lname
    lnameClick()
    pawg.write(("").join(lname))

def insertPassword():
    # insert pw: (391, 396)
    pawg.click(391, 396)
    pawg.write('cultureplay')

def insertPwVerify():
    # click retype: (395, 423)
    pawg.click(395, 423)
    pawg.write('cultureplay')

def insertContext():
    # insert Context into form
    pawg.click(419, 360) #form freezes a couples seconds her sometimes with it's autofill
    time.sleep(1.5)
    contextStr = 'Grandview.Primary.Teachers.eUsers.ERCSD'
    pawg.write(contextStr)

def insertTemplate():
    # templ Checkbox (264, 560)
    pawg.click(264, 560)
    # position of hz scroll bar (407, 718)
    pawg.moveTo(407,718)
    # drag screen to see search button
    pawg.drag(100, 0, .5)
    # click search button (590, 585)
    pawg.click(590, 585)
    # Wait for new window to load, just to be safer
    time.sleep(2.5)
    getTemplate()
    time.sleep(2)


def insertEmail(username, emailCoords=(567,557), okCoords=(442,54)):
    # Move mouse to vertical scroll bar (673, 316)
    pawg.moveTo(673,316)
    # Drag to bottom of form
    pawg.drag(0,200)
    # Click "Add Email"
    pawg.click(emailCoords)
    # Write email address
    pawg.write("".join([username, '@ercsd.org']))
    # Click "OK" to enter
    pawg.click(okCoords)
    #wait here

def processRows(df=campAccts):
    for entry in df.index:
        print("process {}".format(entry))
        obj = df.iloc[entry]

        makeAcct(obj, entry)
        time.sleep(5)

        # Make sure bottom left of form view
        dragBottomLeft()
        time.sleep(5)
        # Submit (Click "OK") (293, 682)
        pawg.moveTo(286, 682)
        pawg.click(286, 682)
        time.sleep(3)
        # Click "Repeat Task" for new entry form (383, 380)
        pawg.moveTo(383, 380)
        pawg.click(383,380) 
        time.sleep(2)         

def processSingleRow(df=campAccts, rowNum=0):
    pass

def acctIsNull(teacher):
    # "Search" tab (546,77)
    pawg.click(546,77)
    # Search field (432, 205)
    pawg.click(432,205)
    pawg.write(teacher)
    # Search button (529, 416)
    pawg.click(529, 416)
    resp = input()
    return resp
    
# Enter user list in here (last name *lname* works better)
def acctExists():
    teachers = ['bbarrow', 'nborno', 'oborno', 'sestevez', 'kgarcia', 'jgilles', 'sgilles', 'scelestin', 'mhenriquez', 'jhernandez', 'lkilkenny', 'glabaze', 'clouise', 'slugo', 'smcdonald', 'cmendez', 'mmend', 'pmores', 'cnorman', 'msewnath', 'jsimpson', 'cthomas']
    teachFrame = pd.DataFrame(columns=[teachers, 'Exists?'])
    for t in teachers:
        teacherIsNull(t)
        #time.sleep(3)

    print(teachFrame)

def dragBottomLeft():
    # Move mouse to vertical scroll bar (673, 316)
    #pawg.moveTo(673,316)
    # it clicks back up, then messes up the drag, leave out for now, reposition lower if doing
    # Drag to bottom of form
    #pawg.drag(0,200,.5)
    # Move mouse to hz scroll bar (407, 718)
    pawg.moveTo(407, 718)
    # Drag screen left to see "OK" submit btn
    pawg.drag(-100, 0, .5)

if __name__ == "__main__":
    processRows()
    #processSingleRow(rowNum=0)
