from datetime import datetime

def is_future(date_str):

    date_format = "%d/%m/%Y"
    # convert the string to a datetime object
    input_date = datetime.strptime(date_str, date_format)

    # get today's date
    today = datetime.today()
    
    # compare and return result
    return input_date.date() > today.date()


# The beloe can also work for the date validation (confirm with ore how it can work for a specific date)

    # # Date validation
    # min_date = datetime.today()

    # if flight_date:
    #     selected_date = datetime.strptime(depDate,"%d/%m/%Y")

    #     # Validate if the selected date is after today
    #     if selected_date > min_date:
    #         print("Valid date selected. Proceeding with booking.")

    #     else:
    #         print("Error: You can only select a flight date after present day")
    
    # else:
    #     print("No date selected")
