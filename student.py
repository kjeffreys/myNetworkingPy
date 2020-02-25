"""
@see https://docs.python.org/3/tutorial/classes.html
"""
class Student:
    """
    A student obj with fName, lName, lunch, grade)
    """
    def __init__(self, fName, lName, lunch, grade):
          self.fName = fName;
          self.lName = lName;
          self.lunch = lunch;
          self.grade = grade;

"""
Success!:
>>> kid1 = Student('ky','je', 1, 4)
>>> kid1
<__main__.Student object at 0x00000246D012EE50>
"""
# could extend to inherit with schools