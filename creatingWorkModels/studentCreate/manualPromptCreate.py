import formattedStudent as foStu

def main():
    moreStudents = True
    allStudents = []

    while(moreStudents == True):
        # TODO: Code for loop
        tempStudent = foStu.FormattedStudent()
        tempStudent.setFname = studentFname()
        tempStudent.setLname = studentLname()
        tempStudent.setFullname = studentFullname()
        tempStudent.setUsername = studentUsername()
        tempStudent.setLunchID = studentLunchID()
        tempStudent.setPW = studentPW()
        tempStudent.setGrade = studentGrade()
        tempStudent.setContext = studentContext()
        tempStudent.setVolume = studentVolume()

        moreStudents = moreStudentsPrompt()




def moreStudentsPrompt():
    print("Are there more students to enter? ( y / n ) ")
    answer = input()
    if(answer == 'n' or answer == 'N' or answer == "No"):
        return False
    else:
        return True

def studentFname()
def studentLname()
def studentFullname()
def studentUsername()
def studentLunchID()
def studentPW()
def studentGrade()
def studentContext()
def studentVolume()







if __name__ == '__main__':
    main()

