FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temperature = float(input("Enter the temperature to convert: "))
    choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if choice == 'C':
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is: {converted_temperature}°F")
    elif choice == 'F':
        converted_temperature = convert_to_celsius(temperature)
        print(f"{temperature}°F is: {converted_temperature}°C")
    else:
        print("Invalid choice. Please try again.")
 

if __name__ == "__main__":
    main()
