# Filename: cwa1a.py
# Author: Chua Yu Peng
# Description: Creates a new STAFF.DAT file.
import datetime
import os
import re

def CREATESTAFF():
    try:
        if os.path.exists("STAFF.DAT"):
            StaffFile = open("STAFF.DAT", "w")
            print("STAFF.DAT overwritten due to program specifications.")
        else:
            StaffFile = open("STAFF.DAT", "w")
            print("New STAFF.DAT created.")

        Date = datetime.datetime.today()
        LastUpdateDate = Date.strftime("%d-%m-%Y")

        ValidNoOfRecords = False
        while not ValidNoOfRecords:
            NoOfRecords = input("Enter Number of Records: ")
            if len(NoOfRecords) == 0:
                print("Empty Input. Try Again.")
            elif not NoOfRecords.isdigit():
                print("Number of Records must be all digits. Try Again.")
            elif int(NoOfRecords) < 1:
                print("Invalid Number of Records. Try Again.")
            else:
                ValidNoOfRecords = True

        StaffFile.write(LastUpdateDate + NoOfRecords + "\n")

        i = int(NoOfRecords)
        StaffIDPattern = re.compile("[12][0-1][89012][0-9]{2}")
        NamePattern = re.compile("[A-Za-z!@:']+")
        EmployeeTypePattern = re.compile("[TtSs]")
        while i > 0:
            ValidStaffID = False
            while not ValidStaffID:
                StaffID = input("Enter Staff ID: ")
                if len(StaffID) == 0:
                    print("Empty Input. Try Again.")
                elif not StaffID.isdigit():
                    print("StaffID must be all digits. Try Again.")
                elif len(StaffID) != 5:
                    print("Staff ID must be 5 digits long. Try Again.")
                elif int(StaffID[3:5]) == 0:
                    print("StaffID does not match implicit requirements. Try Again.")
                elif not StaffIDPattern.match(StaffID):
                    print("StaffID does not match implicit requirements. Try Again.")
                else:
                    ValidStaffID = True

            ValidName = False
            while not ValidName:
                Name = input("Enter Name: ")
                if len(Name) == 0:
                    print("Empty Input. Try Again.")
                elif len(Name) > 35:
                    print("Name must not be more than 35 characters. Try Again.")
                elif not NamePattern.match(Name):
                    print("Name can only be alphabets and ! @ : '. Try Again.")
                else:
                    ValidName = True

            ValidEmployeeType = False
            while not ValidEmployeeType:
                EmployeeType = input("Enter Employee Type: ")
                if len(EmployeeType) == 0:
                    print("Empty Input. Try Again.")
                elif not EmployeeTypePattern.match(EmployeeType):
                    print("Employee Type can only be 1 character long, and either T or S. Try Again.")
                else:
                    EmployeeType = EmployeeType.upper()
                    ValidEmployeeType = True
            
            StaffFile.write("{0:5s}{1:35s}{2:1s}".format(StaffID, Name, EmployeeType) + "\n")
            i = i - 1

        StaffFile.close()
        
    except IOError:
        print("Unable to write to STAFF.DAT.")



if __name__ == "__main__":
    CREATESTAFF()
