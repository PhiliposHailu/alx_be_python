from datetime import datetime
import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    return f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}"

def calculate_future_date():

    number_of_days = int(input("Enter the number of days to add to the current date: "))
    tdelta = datetime.timedelta(days = number_of_days)
    future_date = (datetime.date.today()) + tdelta
    return f"Future date: {future_date.strftime('%Y-%m-%d')}"

print(display_current_datetime())
print(calculate_future_date())

