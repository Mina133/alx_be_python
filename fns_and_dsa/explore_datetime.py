import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current date and time:", current_date)



def  calculate_future_date(numberOfDays):
    future_date = datetime.datetime.now() + datetime.timedelta(days=numberOfDays)
    future_date = future_date.strftime("%Y-%m-%d")
    print("Future date:", future_date)

def main():
    display_current_datetime()
    numberOfDays = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(numberOfDays)


if __name__ == "__main__":
    main()