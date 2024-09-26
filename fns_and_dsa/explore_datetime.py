from datetime import datetime

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")  

def calculate_future_date(number_of_days):
   
    future_date = datetime.now() + datetime.timedelta(days=number_of_days)
    future_date_formatted = future_date.strftime("%Y-%m-%d")  
    print(f"Future date ({number_of_days} days from now): {future_date_formatted}")

def main():
    display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(number_of_days)

if __name__ == "__main__":
    main()