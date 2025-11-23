from datetime import datetime, timedelta

def display_current_datetime():
    """
    Gets the current local date and time and formats it using
    the required 24-Hour format (%H)
    """
    current_date = datetime.now()

    format_string = "%Y-%m-%d %H:%M:%S"
    formatted_date = current_date.strftime(format_string)
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates the future date.
    """
    try:
        prompt_message = "Enter the number of days to add to the current date: "
        number_of_days = int(input(prompt_message))
        
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return
    
    future_date = datetime.now() + timedelta(days=number_of_days)

    format_string = "%Y-%m-%d"

    formatted_date = future_date.strftime(format_string)
    print(f"Future date: {formatted_date}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()