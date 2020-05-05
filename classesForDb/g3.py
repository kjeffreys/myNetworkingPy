import ancillaryStudent as a2

class G3(a2.AncillaryStudent):

    def __init__(self):
        #grade = '3'
        #code = '29'
        contextAdd = '29.Primary.'
        a2.AncillaryStudent.__init__(self)
        self.context = contextAdd + self.context
        self.template = 'User_Template.29.Primary.Students.eUsers.ERCSD'
        


