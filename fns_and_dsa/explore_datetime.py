from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def display_current_datetime():
    kenya_tz = ZoneInfo("Africa/Nairobi")
    current_date = datetime.now(kenya_tz)

    format_string = "%Y-%m-%d %I:%M:%S"
    formatted_date = current_date.strftime(format_string)
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=number_of_days)

    format_string = "%Y-%m-%d"

    formatted_date = future_date.strftime(format_string)
    print(f"Future date: {formatted_date}")

display_current_datetime()
calculate_future_date()