import eUsers

class Student(eUsers.User):

    def __init__(self):
        eUsers.User.__init__(self)
        self.grade = ' '
        self.gradeCode = ' '
        self.lunchID = ' '

    def getLunchID(self):
        return self.lunchID
        
    def setLunchID(self, lunch):
        self.lunchID = lunch

    def getGrade(self):
        return self.grade
        
    def setGrade(self, grade):
        self.grade = grade
        self.setGradecode(grade)

    def getGradecode(self):
        return self.gradeCode
        
    def setGradecode(self, grade):
        gradeDict = {'K': '32', '1':'31', '2':'30', '3':'29', '4':'28','5':'27', '6':'26', '7':'25', '8':'24'}
        self.gradeCode = gradeDict['grade']

    def setParsedName(self, name, pw):
        parsed = name.split()
        self.fName = parsed[0]
        self.lName = parsed[-1]
        self.password = pw
        username = parsed[0][0].upper() + parsed[-1][0].upper() + pw
        self.username = username
        print("setParsedName()")

        

