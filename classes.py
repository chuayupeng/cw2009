# Filename: classes.py
# Name: Chua Yu Peng
# Description: Implements suitable class relationship for Staff, between Teaching and Support Staff.

class Staff():
    ''' superclass for staff '''
    def __init__(self, StaffID, Name, EmployeeType):
        ''' define variables '''
        self.__StaffID = StaffID
        self.__Name = Name
        self.__EmployeeType = EmployeeType
  
    ''' getty '''
    def getStaffID(self):
        return self.__StaffID
    
    def getName(self):
        return self.__Name
    
    def getEmployeeType(self):
        return self.__EmployeeType

    ''' setty '''
    def setName(self, newName):
        self.__Name = newName
    
    def setEmployeeType(self, newEmployeeType):
        self.__EmployeeType = newEmployeeType

    ''' show all '''
    def display(self):
        return ("{0:5s}{1:35s}{2:1s}".format(self.__StaffID,self.__Name, self.__EmployeeType))

class Teaching(Staff):
    ''' subclass for staff '''
    def __init__(self, StaffID, Name, EmployeeType, CourseCode1, CourseCode2, CourseCode3):
        ''' define variables '''
        super().__init__(StaffID, Name, EmployeeType)
        self.__CourseCode1 = CourseCode1
        self.__CourseCode2 = CourseCode2
        self.__CourseCode3 = CourseCode3
        
    ''' getty '''
    def getCourseCode1(self):
        return self.__CourseCode1
    def getCourseCode2(self):
        return self.__CourseCode2
    def getCourseCode3(self):
        return self.__CourseCode3

    ''' setty '''
    def setCourseCode1(self, newCourseCode1):
        self.__CourseCode1 = newCourseCode1
    def setCourseCode2(self, newCourseCode2):
        self.__CourseCode2 = newCourseCode2
    def setCourseCode3(self, newCourseCode3):
        self.__CourseCode3 = newCourseCode3

    ''' show all '''
    def display(self):
        return ("{0:41s}{1:4s}{2:4s}{3:4s}{4:3s}{5:3s}".format(super().display(),self.__CourseCode1,self.__CourseCode2,self.__CourseCode3, "NIL", "NIL"))

class Support(Staff):
    ''' subclass for staff '''
    def __init__(self, StaffID, Name, EmployeeType, SubjectArea1, SubjectArea2):
        ''' define variables '''
        super().__init__(StaffID, Name, EmployeeType)
        self.__SubjectArea1 = SubjectArea1
        self.__SubjectArea2 = SubjectArea2
        
    ''' getty '''
    def getSubjectArea1(self):
        return self.__SubjectArea1
    def getSubjectArea2(self):
        return self.__SubjectArea2

    ''' setty '''
    def setSubjectArea1(self, newSubjectArea1):
        self.__SubjectArea1 = newSubjectArea1
    def setSubjectArea2(self, newSubjectArea2):
        self.__SubjectArea2 = newSubjectArea2

    ''' show all '''
    def display(self):
        return ("{0:41s}{1:4s}{2:4s}{3:4s}{4:3s}{5:3s}".format(super().display(),"NIL", "NIL", "NIL",self.__SubjectArea1,self.__SubjectArea2))
