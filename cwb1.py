# Filename: cwb1.py
# Author: Chua Yu Peng
# Description: Displays the content of STAFF.DAT

import datetime
import os

def DISPLAYSTAFF():
    if os.path.exists("STAFF.DAT"):
        StaffFile = open("STAFF.DAT", "r")
        FirstLine = StaffFile.readline()
        Date = FirstLine[0:10]
        LastUpdateDate = datetime.datetime.strptime(Date, "%d-%m-%Y").strftime("%y%m%d")
        print("Last update: ", LastUpdateDate)
        NoOfRecords = FirstLine[10:]
        print("#Records: ", NoOfRecords)
        print("{0:15s}{1:36s}{2:15s}".format("StaffID", "Name", "EmployeeType"))
        print("-"*66)
        for Record in StaffFile.readlines():
            StaffID = Record[0:5]
            Name = Record[5:40]
            EmployeeType = Record[40:41]
            if EmployeeType == "T":
                EmployeeType = "Teacher"
            elif EmployeeType == "S":
                EmployeeType = "Support"
            print("{0:15s}{1:36s}{2:15s}".format(StaffID, Name, EmployeeType))
    else:
        print("STAFF.DAT does not exist.")
            


if __name__ == "__main__":
    DISPLAYSTAFF()

