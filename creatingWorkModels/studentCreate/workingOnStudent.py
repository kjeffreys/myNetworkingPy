
class Student:
    category = "Student"
    schools = ["CHR, ELD, FLE, MAR"]

    def __init__(self):
        print("Student created")
        self.fname = " "
        self.lname = " "
        self.lunch = " "
        self.pw = " "
        self.username = " "
        self.school = " "
        self.grade = " "

    def setNameLunch(self, info):
        self.info = info.split()
        print('1: {} 2: {} 3: {}'.format(self.info[0], self.info[1], self.info[2] ) )
        self.fname = self.info[0]
        self.lname = self.info[1]
        self.lunch = self.info[2]
        self.pw = self.info[2]
        #working so far
    
    def setByPrompt(self):
        print("Enter name length (2,3)")
        data = input()
        components = data.split()
        for i in range(len(components)):
            print("Element {}: {}".format(i, components[i]))

    #short prompt to save typing
    def prm(self):
        print('Enter info:')
        data1 = input()
        components = data1.split()
        print(components)

        print("Name only or name and id? ([1 for NO], [2 for name AND id]")
        # NOTE: Had issue where if not using int, the conditionals will not execute
        # Python reads the input as a string. Does not convert to a number unless told to do so for logical evaluations
        data2 = int(input())

        print("For name...Enter 2 if len=2(fname, lname), Enter 3 if len=3(fname, paternal, maternal)")
        nameLen = int(input())



        #lunch id not provided
        if(data2 == 1):
            self.fname = components[0]
            if(nameLen == 2):
                self.lname = components[1]
                print("I'm in data2==1 and nameLen==2")
            elif(nameLen == 3):
                paternal = components[1]
                maternal = components[2]
                self.lname = " ".join([paternal, maternal])
                #working up to here
                
                #print("I'm in data2==1 and nameLen==3")
        #lunch id provided
        elif(data2 == 2):
            self.fname = components[0]
            if(nameLen == 2):
                self.lname = components[1]
                self.lunch = components[2]
                self.pw = components[2]
                self.username = "".join([components[0][0],components[1][0],components[2]])
                print("I'm in data2==2 and nameLen==2")
            if(nameLen == 3):
                self.fname = components[0]
                self.lname = " ".join([components[1], components[2]])
                self.lunch = components[3]
                self.pw = components[3]
                self.username = "".join([components[0][0],components[1][0],components[3]])
                #print("I'm in data2=2 and nameLen==3")

        print("Successful execution of prm (prompt setting of student)")

    def myVals(self):
        print("Username: {}".format(self.username))
        print("First name: {}".format(self.fname))
        print("Last name: {}".format(self.lname))
        print("Password: {}".format(self.lunch))
        '''
        >>> my.myVals()
        Username: HD889521
        First name: Henry
        Last name: Duarte Perez
        Password: 889521
        '''
    def setGrade(self, grade):
        self.grade = grade

    def setSchool(self, school):
        self.school = school


'''
Note:
Remember to create an object of the class Student,
using module student. So:
newStudent = student.Student('str1', 4)
'''


