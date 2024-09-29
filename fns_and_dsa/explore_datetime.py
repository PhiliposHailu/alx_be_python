from datetime import datetime
import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")

def calculate_future_date():

    number_of_days = int(input("Enter the number of days to add to the current date: "))
    tdelta = datetime.timedelta(days = number_of_days)
    future_date = (datetime.date.today()) + tdelta
    print(f"Future date: {future_date}")

display_current_datetime()
calculate_future_date()
