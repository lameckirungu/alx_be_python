FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using global factor."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global factor."""
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
    return fahrenheit

def conversion():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    units = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    match units:
        case 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted_temp}°F")
        case 'F':
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature:.1f}°F is {converted_temp}°C")
        case _:
                print("Invalid unit. Choose C for Celsius or F for fahrenheit!")


if __name__ == "__main__":
    conversion()