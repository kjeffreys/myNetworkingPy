"""
@see https://docs.python.org/3/tutorial/classes.html
"""
def makeNewStudent():
    g = eval(input("Enter student\n"))
    el = g.split()
    print(g)
    print(el)

'''
class Student:
    # username = ""  # stud=fInit+lInit+lunch
    # pw = ""
    context = ""
    template = ""
    volume = ""
    homeDir = ""
    first = 'hi'
    """
    A student obj with fName, lName, lunch, grade)
    """
'''
'''
    def __init__(self, 
        self.fName = args[0]
        self.lName = args[1]
        self.lunch = args[2]
        self.username = args[0][0] + args[1][0] + args[2][0]
        self.pw = args[2]

    def setGrade(self, grade):
        gradeMap = {"K": "32", "1": "31", "2": "30",
                    "3": "29", "4": "28", "5": "27", "6": "26", "7": "25",
                    "8": "24"
                    }
        self.grade = grade

        # K~32 1~31 2~30 3~29 4~28 5~27 6~26 7~25 8~26
        self.adjustedGrade = gradeMap[grade]

        # Context (5th)grade = 27.Intermediate.Students.eUsers.ERCSD
        contextVars = [self.adjustedGrade,
                       "Intermediate", "Students", "eUsers.ERCSD"]
        self.context = ".".join(contextVars)

        # Template:(5th) user_template.27.Intermediate.Students.eUsers.ERCSD
        self.template = ".".join(
            "user_template", self.adjustedGrade, "Intermediate", "Students", "eUsers.ERCSD")

        # Volume: (5th)50-int-fs_VOL1.Servers.ERCSD
        self.volume = ("50-int-fs_VOL1" + ".Servers.ERCSD")

        # Path: \HOMEDIRS\STUDENTS\2027\
        self.homeDir = "\\".join("HOMEDIRS", "STUDENTS", "2027")

    def prSt(self):
        print(self.username)
        print(self.fname)
        print(self.lname)
        print(self.context)
        print(self.template)
        print(self.volume)
        print(self.homeDir)


"""
Success!:
>>> kid1 = Student('ky','je', 1, 4)
>>> kid1
<__main__.Student object at 0x00000246D012EE50>
"""
# could extend to inherit with schools
'''