import os
from datetime import timedelta
import datetime
import sys
import shutil

#utility
def withLeftMarginPointer(string):
    """
    The function adds a left margin of spaces to a given string.
    """
    return f"       {string}"

#utility
def withLeftMargin(string):
    """
    The function `withLeftMargin` adds a left margin of 8 spaces to a given string..
    """
    return f"        {string}"

def withMargin(string):
    """
    The function `withLeftMargin` adds a left margin of 8 spaces to a given string..
    """
    return f"        {string}        "

#utility
def clear():
    """
    The clear function clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    

#utility
def indexFinder(varList, ID):
    """
    The function "indexFinder" takes in a list and an ID, and returns the index of the first occurrence
    of the ID in the list.
    
    :param varList: A list of variables or values
    :param ID: The ID parameter is the value that you want to find in the varList
    :return: The index of the first occurrence of the ID in the varList.
    """
    for index in range(0, len(varList)):
        if varList[index] == ID:
            return index

#utility
def dateRange(startDate, endDate):
    """
    The function `dateRange` generates a range of dates between a given start date and end date.
    
    :param startDate: The start date of the date range. It is the date from which the range will start
    generating dates
    :param endDate: The `endDate` parameter is the date that marks the end of the date range
    """
    current_date = startDate
    while current_date <= endDate:
        yield current_date.strftime('%Y-%m-%d')
        current_date += timedelta(days=1)  

def main():
    globalVariable() 
    employeeInfoContainer()
    header("CC03 DAILY-TIME RECORD SYSTEM", 120, 13)
    mainMenu()

def globalVariable():
    """
    The function declares global variables for formatted time, formatted date, ask start date, and ask
    end date.
    """
    global formattedTime, formattedDate, currentDate, currentStrDate
    global askStartDate, askEndDate
    global timeIn, timeOut

def employeeInfoContainer():
    """
    The function `employeeInfoContainer` initializes global variables to store employee information.
    """
    global empID,empFirstName, empLastName,empDepartment, empPosition, empTotalHours, empTotalAbsent, empDateStart, empDateEnd
    empID = []
    empFirstName = []
    empLastName = []
    empDepartment = []
    empPosition = []
    empTotalHours = []
    empTotalAbsent = []
    empDateStart = []
    empDateEnd = []

def header(title, width, height):
    """
    The `header` function sets the console size, gets the current date and time, and prints a formatted
    header with the title, date, and time.
    """
    global currentDate
    setConsoleSize(width, height)
    currentDatetime = datetime.datetime.now()
    currentStrDate = currentDatetime.strftime("%Y-%m-%d")
    currentDate = datetime.datetime.strptime(currentStrDate,"%Y-%m-%d")
    global formattedTime, formattedDate
    formattedTime = currentDatetime.strftime('%I:%M:%S' + ' %p').lstrip('0')
    formattedDate = currentDatetime.strftime('%m/%d/%Y')
    print(f"        ==================================== {title} =====================================        ")
    print(withLeftMargin(f"                                                                       {formattedDate} {formattedTime}"))
    
def setConsoleSize(width, height):
    """
    Safely sets the console window size. On Windows, uses 'mode con'.
    On Unix systems, attempts to use 'resize' if available. Silently fails if not supported.
    """
    try:
        if os.name == 'nt':
            os.system(f'mode con cols={width} lines={height}')
        else:
            # Check if 'resize' is available
            if shutil.which('resize'):
                os.system(f'resize -s {height} {width}')
            else:
                # resize not found; skip resizing
                pass
    except Exception:
        pass  


def mainMenu():
    """
    The mainMenu function displays a menu with options for timekeeping, registering an employee, viewing
    employee information, and exiting the program.
    """
    print(withLeftMargin("1. TIMEKEEPING"))
    print(withLeftMargin("2. REGISTER EMPLOYEE"))
    print(withLeftMargin("3. VIEW EMPLOYEE"))
    print(withLeftMargin("4. EXIT\n"))
    askCode()

def askCode():
    """
    The function `askCode()` takes user input for a menu choice and executes different actions based on
    the choice.
    """
    try:
        menuChoice = int(input(withLeftMargin("Enter your choice here: ")))
        if (menuChoice > 4) or (menuChoice <= 0):
            clear()
            header("CC03 DAILY-TIME RECORD SYSTEM", 120, 13)
            print("")
            print(withLeftMargin("Your input is not valid. Please enter either '1' for Timekeeping, '2' for Register Employee, '3' for View"))
            print(withLeftMargin("Employee, or '4' for Exit.\n"))
            mainMenu()
        else:
            clear()
            if (menuChoice == 1):
                timeKeepingScreen("TIMEKEEPING SCREEN", 110, 40)
            elif(menuChoice == 2):
                registerEmployeeScreen("REGISTER EMPLOYEE", 110, 20)
            elif(menuChoice == 3):
                viewEmployee()
            elif(menuChoice == 4):
                exitScreen("CC03 DAILY-TIME RECORD SYSTEM", 120, 13)
            else:
                header("CC03 DAILY-TIME RECORD SYSTEM", 120, 13)
                mainMenu()
    except Exception as e:
        header("CC03 DAILY-TIME RECORD SYSTEM", 120, 13)
        mainMenu()
        
def timeKeepingScreen(title, width, height):
    """
    The `timeKeepingScreen` function allows the user to enter timekeeping data for employees, including
    their ID, start and end dates, and check-in/check-out times.
    """
    header(title, width, height)        
    askEmployee()

def askEmployee():
    """
    The function `askEmployee` prompts the user to enter an employee ID and checks if the ID is
    registered in the system. If not, it asks the user if they want to register as a new employee.
    """
    
    global askEmpID
    global askToRegister
    
    while True:
        try:
            askEmpID = int(input(withLeftMargin("Enter Employee ID: ")))
            if askEmpID in empID:
                startdate()
                break
            elif askEmpID < 1:
                print(withLeftMargin("Kindly input a positive integer only. For example, '10001' or '10002'.\n"))
                continue
            elif askEmpID not in empID: 
                while True:
                    askToRegister = str(input(withLeftMargin("You are not a registered employee. Do you want to register?[Y/N] ")))
                    if askToRegister == "Y" or askToRegister == "y":
                        clear()
                        registerEmployeeScreen("REGISTER EMPLOYEE", 110, 20)
                        break
                    elif askToRegister == "N" or askToRegister == "n":
                        clear()
                        header("CC03 DAILY-TIME RECORD SYSTEM", 120, 13)
                        mainMenu()
                        break
                    else:
                        continue
            
            else:
                print(withLeftMargin("Only integer values are allowed. For example, '10001' or '10002'.\n"))              
        except Exception as e:
            print(withLeftMargin("Only integer values are allowed. For example, '10001' or '10002'.\n"))
            continue

def startdate():
    """
    The function "startdate" is used to define the start date of a task or project.
    """
    global empInd
    global askStartDate
    empInd = indexFinder(empID,askEmpID)
    global intStartDate
    def isValidDate(date):
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    while True:
        askStartDate = str(input(withLeftMargin("Enter Start Date (YYYY-MM-DD): ")))
        if isValidDate(askStartDate):
            intStartDate = datetime.datetime.strptime(askStartDate, "%Y-%m-%d")
            if intStartDate <= currentDate:
                #((currentDate - intStartDate) > timedelta(days=1))
                if currentDate != intStartDate:
                    empDateStart[empInd].append(askStartDate)
                    break
                else:
                    print(withLeftMargin("The start date should be set to a date that is at least a day before today's date."))
            else:
                print(withLeftMargin("The Start Date should not be set to a future date."))
                continue
        else:
            print(withLeftMargin("INCORRECT START DATE ENTRY. INVALID DATE. TRY AGAIN!"))

    enddate()

def enddate():
    """
    The function `enddate()` prompts the user to enter an end date in the format "YYYY-MM-DD" and
    validates the input before storing it in a variable.
    """
    global intEndDate
    global askEndDate
    def isValidDate(date):
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
            return True
        except:
            return False
    while True:
        askEndDate = str(input(withLeftMargin("Enter End Date (YYYY-MM-DD): ")))
        if isValidDate(askEndDate):
            intEndDate = datetime.datetime.strptime(askEndDate, "%Y-%m-%d")
            if intEndDate <= intStartDate:
                print(withLeftMargin("The End Date you've entered is earlier or the same with your Start Date."))
                continue;
            else:
                if intEndDate <= currentDate:
                    empDateEnd[empInd].append(askEndDate)
                    break;
                else:
                    print(withLeftMargin("The Start Date should not be set to a future date."))
                    continue
        else:
            print(withLeftMargin("INCORRECT END DATE ENTRY. INVALID DATE. TRY AGAIN!"))
            continue;
    
    checkInOut()

def checkInOut():
    """
    The `checkInOut()` function allows the user to input time-in and time-out entries for a specific
    date range, calculates the total hours worked and total absences for each employee, and provides
    options to continue entering timekeeping entries or return to the main menu.
    """
    totalAbsent = 0
    totalHours = 0
    global intTimeIn, intTimeOut
    for date in dateRange(intStartDate, intEndDate):
        print("")
        print(withLeftMargin(">>Date of Entry: " + date))
        print(withLeftMargin(" (Enter 'A' if Absent)"))
        while True:
            shift = str(input(withLeftMargin("Shift Type(Day-Shift or Night-Shift)[D/N]: ")))
            print("")
            if ((shift == "Y" or shift == "y") or (shift == "N" or shift == "n")):
                break
            else:
                print(withLeftMargin("Please enter 'D' or 'N' only."))
                continue
        if shift == "D" or shift == "d":
            while True:
                try:
                    timeIn = str(input(withLeftMargin("Enter Time-In: ")))
                    hours, minutes = timeIn.split(':')
                    intTimeIn = datetime.datetime.strptime(f'{timeIn}', '%H:%M')
                    if len(minutes) != 2 or len(hours) != 2:
                        print(withLeftMargin("INCORRECT TIME-IN FORMAT. PLEASE FOLLOW 24-HOUR FORMAT(HH:MM)."))
                        continue
                    
                    while True:
                        try:
                            timeOut = str(input(withLeftMargin("Enter Time-Out: ")))
                            hours, minutes = timeOut.split(':')
                            intTimeOut = datetime.datetime.strptime(f'{timeOut}', '%H:%M')
                            if len(minutes) != 2  or len(hours) != 2:
                                print(withLeftMargin("INCORRECT TIME-OUT FORMAT. PLEASE FOLLOW 24-HOUR FORMAT(HH:MM)."))
                                continue
                            else:
                                
                                if intTimeOut <= intTimeIn:
                                    print(withLeftMargin("Time-Out input is earlier or same with Time-In."))
                                    continue
                                else:
                                    timeWorked = intTimeOut - intTimeIn
                                    result = timeWorked.seconds / 3600
                                    totalHours += result
                                    break
                        except Exception as e:
                            print(withLeftMargin("INCORRECT TIME-OUT FORMAT. PLEASE FOLLOW 24-HOUR FORMAT(HH:MM)."))
                            continue
                    break
                except Exception as e:
                    if timeIn == "A" or timeIn == "a":
                        totalAbsent += 1
                        while True:
                            timeOut = input(withLeftMargin("Enter Time-Out: "))
                            if timeOut == "A" or timeOut == "a":
                                break
                            else:
                                print(withLeftMargin("Enter 'A' if Absent"))
                                continue       
                    else:
                        print(withLeftMargin("INCORRECT TIME-IN FORMAT. PLEASE FOLLOW 24-HOUR FORMAT(HH:MM)."))
                        continue
                    break
        else:
            while True:
                try:
                    timeIn = str(input(withLeftMargin("Enter Time-In: ")))
                    hours, minutes = timeIn.split(':')
                    if datetime.datetime.strptime(f'{timeIn}', '%H:%M') <= datetime.datetime.strptime('12:00', '%H:%M'):
                        intTimeIn = datetime.datetime.strptime(f'{timeIn} {date}', '%H:%M %Y-%m-%d') + timedelta(days=1)
                        
                    else:
                        intTimeIn = datetime.datetime.strptime(f'{timeIn} {date}', '%H:%M %Y-%m-%d')
                        if not intTimeIn < datetime.datetime.strptime(f'18:00 {date}', '%H:%M %Y-%m-%d'):
                            pass
                        else:
                            print(withLeftMargin("Night shift should start by 18:00 and end by 06:00."))
                            continue
                    if len(minutes) != 2 or len(hours) != 2:
                        print(withLeftMargin("INCORRECT TIME-IN FORMAT. PLEASE FOLLOW 24-HOUR FORMAT(HH:MM)."))
                        continue
                    
                    while True:
                        try:
                            timeOut = str(input(withLeftMargin("Enter Time-Out: ")))
                            hours, minutes = timeOut.split(':')
                            intTimeOut = datetime.datetime.strptime(f'{timeOut}', '%H:%M')
                            if intTimeIn == (datetime.datetime.strptime(f'{timeIn} {date}', '%H:%M %Y-%m-%d') + timedelta(days=1)):
                                intTimeOut = datetime.datetime.strptime(f'{timeOut} {date}', '%H:%M %Y-%m-%d') + timedelta(days=1)
                            elif datetime.datetime.strptime(f'{timeOut}', '%H:%M') <= datetime.datetime.strptime('12:00', '%H:%M'):
                                intTimeOut = datetime.datetime.strptime(f'{timeOut} {date}', '%H:%M %Y-%m-%d') + timedelta(days=1)
                            else:
                                intTimeOut = datetime.datetime.strptime(f'{timeOut} {date}', '%H:%M %Y-%m-%d')
                                if not intTimeIn < datetime.datetime.strptime(f'18:00 {date}', '%H:%M %Y-%m-%d'):
                                    pass
                                else:
                                    print(withLeftMargin("Night shift should start by 18:00 and end by 06:00."))
                                    continue
                            if len(minutes) != 2  or len(hours) != 2:
                                print(withLeftMargin("INCORRECT TIME-OUT FORMAT. PLEASE FOLLOW 24-HOUR FORMAT(HH:MM)."))
                                continue
                            else:
                                
                                if intTimeOut <= intTimeIn:
                                    print(withLeftMargin("Time-Out input is earlier or same with Time-In."))
                                    continue
                                else:
                                    timeWorked = intTimeOut - intTimeIn
                                    result = timeWorked.total_seconds() / 3600
    
                                    totalHours += result
                                    break
                        except Exception as e:
                            print(withLeftMargin("INCORRECT TIME-OUT FORMAT. PLEASE FOLLOW 24-HOUR FORMAT(HH:MM)." + str(e)))
                            continue
                    break
                except Exception as e:
                    if timeIn == "A" or timeIn == "a":
                        totalAbsent += 1
                        while True:
                            timeOut = input(withLeftMargin("Enter Time-Out: "))
                            if timeOut == "A" or timeOut == "a":
                                break
                            else:
                                print(withLeftMargin("Enter 'A' if Absent"))
                                continue       
                    else:
                        print(withLeftMargin("INCORRECT TIME-IN FORMAT. PLEASE FOLLOW 24-HOUR FORMAT(HH:MM)."))
                        continue
                    break
            
                

    empTotalHours[empInd].append(totalHours)
    empTotalAbsent[empInd].append(totalAbsent)
    totalAbsent = 0
    totalHours = 0
    while True:  
        print("")
        ask = str(input(withLeftMargin("Do you want to place another timekeeping entry? (Y/N): ")))
        if ask == "Y" or ask == "y":
            print("")
            askEmployee()
            break
            
        elif ask == "N" or ask == "n":
            clear()
            header("CC03 DAILY-TIME RECORD SYSTEM", 120, 13)
            mainMenu()
            break
            
        else:
            print(withLeftMargin("Please enter 'Y' or 'N' only."))
            continue  

def registerEmployeeScreen(title, width, height):
    """
    The function "registerEmployeeScreen" takes in parameters for the title, width, and height of a
    screen, and then prompts the user to enter employee details such as first name, last name,
    department, and position.
    """
    header(title, width, height)
    print(withLeftMarginPointer(">>Employee Details"))
    isIDIntAvailable()
    while True:
        registerFname = str(input(withLeftMargin("Enter First Name: "))).upper()
        splitParts = registerFname.split()
        if all(name.isalpha() for name in splitParts):
            empFirstName.append(registerFname)
            break  
        else:
            print(withLeftMargin("Invalid Entry! Please enter a valid First Name."))
            continue
    while True:
        registerLname = str(input(withLeftMargin("Enter Last Name: "))).upper()
        splitLParts = registerLname.split()
        if all(name.isalpha() for name in splitLParts):
            empLastName.append(registerLname)
            break
        else:
            print(withLeftMargin("Invalid Entry! Please enter a valid Last Name."))
            continue
    isDepValid()
    isPosValid()
    empTotalHours.append([])
    empTotalAbsent.append([])
    empDateStart.append([])
    empDateEnd.append([])
    whatTodo()

def isIDIntAvailable():
    """
    The function `isIDIntAvailable()` prompts the user to enter an employee ID as an integer, checks if
    the ID is already in use, and recursively calls itself until a unique ID is entered.
    """
    while True:
        try:
            registerID = int(input(withLeftMargin("Enter Employee ID: ")))
            if registerID not in empID:
                if registerID > 0:
                    empID.append(registerID) 
                    return
                else:
                    print(withLeftMargin("Negative Integers are not valid! Try again!"))
                    continue
            else:
                print(withLeftMargin(f"ID '{registerID}' is not available. Please try again.\n"))
                print(withLeftMarginPointer(">>Employee Details"))
                continue
        except Exception as e:
            print(withLeftMargin("Please enter only integer value. Ex. '10001', '10002'.\n"))
            print(withLeftMarginPointer(">>Employee Details"))
            continue

def isDepValid():
    """
    The function `isDepValid()` prompts the user to enter a department (either 1 for Faculty or 2 for
    Non-Faculty) and validates the input.
    :return: The function isDepValid() does not explicitly return anything.
    """
    while True:
        try:
            registerDep = int(input(withLeftMargin("Enter Department (1)Faculty (2)Non-Faculty: ")))
            if ((registerDep < 3) and (registerDep > 0)):
                if registerDep == 1:
                    empDepartment.append("Faculty")
                    return
                else:
                    empDepartment.append("Non-Faculty")
                    return
            else:
                print(withLeftMargin("Please enter '1' or '2'only.\n"))
                continue  
        except:
            print(withLeftMargin("Please enter either '1' for Faculty or '2' for Non-Faculty.\n"))
            continue

def isPosValid():
    """
    The function `isPosValid()` prompts the user to enter a position (1 for Full-Time or 2 for
    Part-Time) and validates the input.
    :return: The function isPosValid() does not explicitly return anything. However, it appends a value
    to the empPosition list if the input is valid.
    """
    while True:
        try:
            registerPos = int(input(withLeftMargin("Enter Position (1)Full-Time (2)Part-Time: ")))
            if ((registerPos < 3) and (registerPos > 0)):
                if registerPos == 1:
                    empPosition.append("Full-Time")
                    return
                else:
                    empPosition.append("Part-Time")
                    return
            else:
                print(withLeftMargin("Please enter '1' or '2'only.\n"))
                continue  
        except:
            print(withLeftMargin("Please enter either '1' for Full-Time or '2' for Part-Time.\n"))
            continue

def whatTodo():
    """
    The function `whatTodo()` prompts the user to register another employee and collects their details
    if the user chooses to do so, otherwise it returns to the main menu.
    """
    while True:
        print(withLeftMargin(""))
        askToDo = str(input(withLeftMargin("Do you want to register another employee? [Y/N]: ")))
        print(withLeftMargin(""))
        if askToDo == "Y" or askToDo == "y":
            print(withLeftMarginPointer(">>Employee Details"))
            isIDIntAvailable()
            while True:
                registerFname = str(input(withLeftMargin("Enter First Name: "))).upper()
                splitParts = registerFname.split()
                if all(name.isalpha() for name in splitParts):
                    empFirstName.append(registerFname)
                    break  
                else:
                    print(withLeftMargin("Invalid Entry! Please enter a valid First Name."))
                    continue
            while True:
                registerLname = str(input(withLeftMargin("Enter Last Name: "))).upper()
                splitLParts = registerLname.split()
                if all(name.isalpha() for name in splitLParts):
                    empLastName.append(registerLname)
                    break
                else:
                    print(withLeftMargin("Invalid Entry! Please enter a valid Last Name."))
                    continue
            isDepValid()
            isPosValid()
            empTotalHours.append([])
            empTotalAbsent.append([])
            empDateStart.append([])
            empDateEnd.append([])
            whatTodo()
            return
        elif askToDo == "N" or askToDo == "n":
            clear()
            header("CC03 DAILY-TIME RECORD SYSTEM", 120, 13)
            mainMenu()
            return
        else:
            continue

def viewEmployee():
    """
    The `viewEmployee` function allows the user to view the details and timekeeping entries of an
    employee by entering their ID.
    """
    
    setConsoleSize(80,50)
    print(withLeftMargin("========================= View Employee ========================="))
    print(withLeftMargin(f"                                           {formattedDate} {formattedTime}"))
    while True:
        try:
            viewEmp = int(input(withLeftMargin("Enter Employee ID: ")))
            
            if viewEmp not in empID:
                if viewEmp < 0:
                    print(withLeftMargin("Kindly input a positive integer only. For example, '10001' or '10002'.\n"))
                else:
                    while True:
                        askRegister = str(input(withLeftMargin("You are not a registered employee. Do you want to register?[Y/N] ")))
                        if askRegister == "Y" or askRegister == "y":
                            clear()
                            registerEmployeeScreen("REGISTER EMPLOYEE", 110, 20)
                            return
                        elif askRegister == "N" or askRegister == "n":
                            clear()
                            header("CC03 DAILY-TIME RECORD SYSTEM", 120, 13)
                            mainMenu()
                            return
                            
                        else:
                            continue
            else:
                break
                
        except Exception as e:
            print(withLeftMargin("Please enter integer value. Ex. '10001', '10002'.\n"))
            continue
    try:
        viewEmpInd = indexFinder(empID, viewEmp)
        print("")
        print(withLeftMarginPointer(">>Employee Details"))
        print(withLeftMargin(f"First Name: {empFirstName[viewEmpInd]}"))
        print(withLeftMargin(f"Last Name: {empLastName[viewEmpInd]}"))
        print(withLeftMargin(f"Department: {empDepartment[viewEmpInd]}"))
        print(withLeftMargin(f"Position: {empPosition[viewEmpInd]}"))
        print("")
        print(withLeftMarginPointer(">>Timekeeping Entries"))
        if len(empDateStart[viewEmpInd]) > 0:
            for index in range(0, len(empDateStart[viewEmpInd])):
                # Extract the first element from the index lists
                startDate = empDateStart[viewEmpInd][index]
                endDate = empDateEnd[viewEmpInd][index]
                totalAbsentEx = empTotalAbsent[viewEmpInd][index]
                totalHoursEx = empTotalHours[viewEmpInd][index]
                print(withLeftMarginPointer(f"*Date Period: {startDate} to {endDate}"))
                print(withLeftMargin(f"Total # of Hours Worked: {totalHoursEx}"))
                print(withLeftMargin(f"Total # Absences: {totalAbsentEx}"))
                print("")
        else:
            print(withLeftMargin("    No Records found."))
    except Exception as e:
        print(withLeftMargin("A problem has occured" + str(e)))

    while True:
        print("")
        askIfView = str(input(withLeftMargin("Do you want to view another employee? (Y/N): ")))
        if askIfView == "Y" or askIfView == "y":
            print("")
            viewEmployee()
            break
        elif askIfView == "N" or askIfView == "n":
            clear()
            header("CC03 DAILY-TIME RECORD SYSTEM", 120, 13)
            mainMenu()
            break
        else:
            print(withLeftMargin("Invalid Input! Try Again!"))
            continue

def exitScreen(title, width, height):
    """
    The function `exitScreen` displays a goodbye message on the screen with a specified title, width,
    and height.
    """
    header(title, width, height)
    print("")
    print("")
    print("")
    print("                                                     GOODBYE!")
    print("")
    print("")
    print("")
    print(withMargin("========================================================================================================"))
    sys.exit()


""" The code below is checking if the current module is being run as the main program. If it is, then it
calls the `main()` function.
"""
if __name__ == "__main__":
    main()