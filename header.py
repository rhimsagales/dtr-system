import datetime
import os
def header(title, width, height):
    """
    The `header` function sets the console size, gets the current date and time, and prints a formatted
    header with the title, date, and time.
    """
    setConsoleSize(width, height)
    currentDatetime = datetime.datetime.now()
    global formattedTime, formattedDate
    formattedTime = currentDatetime.strftime('%I:%M:%S' + ' %p').lstrip('0')
    formattedDate = currentDatetime.strftime('%m/%d/%Y')
    print(f"        ==================================== {title} =====================================        ")
    print(withLeftMargin(f"                                                                       {formattedDate} {formattedTime}"))
    
def setConsoleSize(width, height):
    """
    The function sets the size of the console window in Python.
    
    """
    os.system(f'mode con cols={width} lines={height}')

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

#DITO I CUSTOMIZE YUNG TITLE NG HEADER PATI YUNG WIDTH AND HEIGHT
#First Argument should be a string for title, second argument should be integer to set width and third argument should be integer for height of the console
header("CC03 DAILY-TIME RECORD SYSTEM", 120, 13)


