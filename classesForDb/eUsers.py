class User:    #General superclass
    '''
    Attributes go first
    '''

    '''
    Methods below
    '''
    def __init__(self):
        self.fName = ' '
        self.lName = ' '
        self.password = ' '
        self.context = ' '
        self.template = ' '
        self.volume = ' '
        self.homeDir = ' '
    
    def createUser(self):
        print("createUser()")
    
    def deleteUser(self):
        print("deleteUser()")
    
    def disableAcct(self):
        print("disableAcct()")

    def enableAcct(self):
        print("enableAcct()")

    def modifyUser(self):
        print("modifyUser()")

    def moveUser(self):
        print("moveUser()")
    
    def renameUser(self):
        print("renameUser()")

    def setUsername(self):
        print("setUsername()")

    def setFirstName(self):
        print("setFirstName()")

    def setLastName(self):
        print("setLastName()")

    def setContext(self):
        print("setContext()")

    def setTemplate(self):
        print("setTemplate")
        # Note: some are "User_template". Others are "user_template"
        # Need to map accurately for all or do manually with pyautogui
        # Need to map grade attr also if student.
        # Need to map several other permission templates for admins
    
    def getPassword(self):
        return self.password

    def setPassword(self):
        print("setPassword()")

    def getHomeDir(self):
        return self.homeDir
    def setHomeDir(self):
        print("setHomeDir()")
