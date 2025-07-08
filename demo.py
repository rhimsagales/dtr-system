def calculate_payroll():
    while True:
        clear()
        print_header("Payroll")

        # Asking for Employee ID until a valid one is provided
        while True:
            employee_id = input("Enter Employee ID: ")
            if employee_id not in employee_database:
                print("EMPLOYEE ID DOES NOT EXIST. TRY AGAIN!")
                continue  # Prompt again for the employee ID if it's not in the database
            else:
                break

        while True:
            pay_period_date = input("Enter Pay Period Date (YYYY-MM-DD): ")
            try:
                pay_period_date = datetime.datetime.strptime(pay_period_date, "%Y-%m-%d")
                # Validate pay period date
                strPayPeriodDate = datetime.datetime.strftime(pay_period_date, "%Y-%m-%d")
                if strPayPeriodDate[8:10] not in ["15", "30", "31"]:
                    print("INCORRECT PAY PERIOD DATE ENTRY. MUST BE 15TH AND/OR END OF THE MONTH ONLY. TRY AGAIN!")
                    continue
                else:
                    break
            except ValueError:
                print("INCORRECT PAY PERIOD DATE ENTRY. INVALID DATE ENTRY. TRY AGAIN!")

        formatted_current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        formatted_pay_period_date = pay_period_date.strftime("%Y-%m-%d")
        print(" ")
        print(f"Pay Period Date/s: {formatted_current_date} to {formatted_pay_period_date}")

        while True:
            regular_hours = float(input("Enter Total # of Regular Hours Worked: "))
            overtime_hours = float(input("Enter Total # of Overtime Hours Worked: "))

            if regular_hours <= 0 or overtime_hours < 0:
                print("Invalid input. Regular hours should be greater than 0, and overtime hours should be non-negative.")
            else:
                break  # Break the loop when valid input is provided

        # Perform further calculations or operations with valid input
        # ...

        # Ask for another payroll entry after calculations
        print(" ")
        another_entry = input("Do you want to place another payroll entry? (Y/N): ")
        if another_entry.upper() == 'Y':
            continue  # Go back to entering another payroll entry
        elif another_entry.upper() == 'N':
            return  # Exit from the function and return to the main menu
        else:
            print("Invalid input. Please enter Y for Yes or N for No.")

# Rest of your code remains unchanged.