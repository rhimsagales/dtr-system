```tefcha
askCode
menuChoice
if menuChoice > 4 or menuChoice <= 0
clear
header("CC03 DAILY-TIME RECORD SYSTEM", 120, 13)
display
display "Your input is not valid. Please enter either '1' for Timekeeping, '2' for Register Employee, '3' for View"
display "Employee, or '4' for Exit."
mainMenu
end
if menuChoice == 1
clear
timeKeepingScreen("TIMEKEEPING SCREEN", 110, 40)
end
if menuChoice == 2
clear
registerEmployeeScreen("REGISTER EMPLOYEE", 110, 20)
end
if menuChoice == 3
viewEmployee
end
if menuChoice != 1 and menuChoice != 2 and menuChoice != 3
header("CC03 DAILY-TIME RECORD SYSTEM", 120, 13)
mainMenu
end


