# Filename: cwb2.py
# Author: Chua Yu Peng
# Description: Reads records from STAFF.DAT and writes updated record to USTAFF.DAT

import datetime
import os
import re
from classes import *

def UPDATESTAFF():
    try:
        StaffFile = open("STAFF.DAT", "r")
        
        if os.path.exists("USTAFF.DAT"):
            UStaffFile = open("USTAFF.DAT", "r+")
            AddNoOfRecords = int(UStaffFile.readline()[10:15])
            UStaffFile.seek(0)
        else:
            UStaffFile = open("USTAFF.DAT", "w")
            AddNoOfRecords = 0

        LastUpdateDate = datetime.datetime.today().strftime("%d-%m-%Y")
        NoOfRecords = int(StaffFile.readline()[10:-1])
        NoOfRecords = NoOfRecords + AddNoOfRecords
        
        UStaffFile.write("{0:10s}{1:5s}".format(LastUpdateDate, str(NoOfRecords).zfill(5))+ "\n")
        UStaffFile.seek(0,2)
        
        CourseCodePattern = re.compile("[A-Z]{2}[0-9]{2}")
        SubjectAreaPattern = re.compile("[A-Z]{2}")
        for Record in StaffFile.readlines():
            StaffID = Record[0:5]
            Name = Record[5:40]
            EmployeeType = Record[40:41]
            print("StaffID: ", StaffID)
            print("Name: ", Name)
            if EmployeeType == "T":
                print("Employee Type: Teaching")
                ValidCourseCode1 = False
                while not ValidCourseCode1:
                    CourseCode1 = input("Enter Course Code (1): ")
                    if len(CourseCode1) == 0:
                        print("Empty Input. Try Again.")
                    elif len(CourseCode1) !=4:
                        print("Course Codes should be 4 characters long. Try Again.")
                    elif not CourseCodePattern.match(CourseCode1):
                        print("Course Codes should be comprised of 2 captial letters and 2 digits. Try Again.")
                    else:
                        ValidCourseCode1 = True

                ValidCourseCode2 = False
                while not ValidCourseCode2:
                    CourseCode2 = input("Enter Course Code (2) (optional, Enter without input to proceed): ")
                    if len(CourseCode2) == 0:
                        ValidCourseCode2 = True
                        CourseCode2 = "NIL"
                    elif len(CourseCode2) !=4:
                        print("Course Codes should be 4 characters long. Try Again.")
                    elif not CourseCodePattern.match(CourseCode2):
                        print("Course Codes should be comprised of 2 captial letters and 2 digits. Try Again.")
                    else:
                        ValidCourseCode2 = True

                ValidCourseCode3 = False
                while not ValidCourseCode3:
                    CourseCode3 = input("Enter Course Code (3)(optional, Enter without input to proceed): ")
                    if len(CourseCode3) == 0:
                        ValidCourseCode3 = True
                        CourseCode3 = "NIL"
                    elif len(CourseCode3) !=4:
                        print("Course Codes should be 4 characters long. Try Again.")
                    elif not CourseCodePattern.match(CourseCode3):
                        print("Course Codes should be comprised of 2 captial letters and 2 digits. Try Again.")
                    else:
                        ValidCourseCode3 = True

                Staff = Teaching(str(StaffID), str(Name), str(EmployeeType), str(CourseCode1), str(CourseCode2), str(CourseCode3))            
                        
            elif EmployeeType == "S":
                print("Employee Type: Support")
                ValidSubjectArea1 = False
                while not ValidSubjectArea1:
                    SubjectArea1 = input("Enter Subject Area (1): ")
                    if len(SubjectArea1) == 0:
                        print("Empty Input. Try Again.")
                    elif len(SubjectArea1) !=2:
                        print("Subject Areas should be 2 characters long. Try Again.")
                    elif not SubjectAreaPattern.match(SubjectArea1):
                        print("Subject Areas should be comprised of 2 captial letters. Try Again.")
                    else:
                        ValidSubjectArea1 = True

                ValidSubjectArea2 = False
                while not ValidSubjectArea2:
                    SubjectArea2 = input("Enter Subject Area (2) (optional, Enter without input to proceed): ")
                    if len(SubjectArea2) == 0:
                        ValidSubjectArea2 = True
                        SubjectArea2 = "NIL"
                    elif len(SubjectArea2) !=2:
                        print("Subject Areas should be 2 characters long. Try Again.")
                    elif not SubjectAreaPattern.match(SubjectArea2):
                        print("Subject Areas should be comprised of 2 captial letters. Try Again.")
                    else:
                        ValidSubjectArea2 = True

                Staff = Support(str(StaffID), str(Name), str(EmployeeType), str(SubjectArea1), str(SubjectArea2))            
                

            UStaffFile.write(Staff.display() + "\n")

        UStaffFile.close()
        StaffFile.close()

        
    except IOError:
        print("Unable to read from STAFF.DAT or write to USTAFF.DAT") 

if __name__ =="__main__":
    UPDATESTAFF()

