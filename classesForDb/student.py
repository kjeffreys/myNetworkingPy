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

    def getContext(self):
        return self.context

    def setContext(self, context):
        self.context = context

    def getVolume(self):
        return self.volume

    def setVolume(self, volume):
        self.volume = volume

        

