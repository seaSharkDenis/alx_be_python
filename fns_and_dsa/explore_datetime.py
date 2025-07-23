import datetime
from datetime import timedelta

def display_current_datetime():
    # Part 1
    # Format and print the current date and time in a readable format, such as “YYYY-MM-DD HH:MM:SS”.
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    # Part 2
    # Allow a user to calculate the future date
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    duration = timedelta(days=number_of_days)
    date_today = datetime.datetime.now()

    future_date = date_today + duration
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

    

def main():
    display_current_datetime()
    calculate_future_date()


if __name__ == "__main__":
    main()