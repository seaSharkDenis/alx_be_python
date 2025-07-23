CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def convert_to_celsius(fahrenheit):
    # Takes temperature in fahrenheit and converts to celsius
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    # Takes temperature in celsius and converts to fahrenheit
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temperature_input = float(input("Enter the temperature to convert: "))
        temperature_format = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        if temperature_format == "C":
            converted_temperature = convert_to_fahrenheit(temperature_input)
            print(f"{temperature_input}°C is {converted_temperature}°F")
        elif temperature_format == "F":
            converted_temperature = convert_to_celsius(temperature_input)
            print(f"{temperature_input}°F is {converted_temperature}°C")
        else:
            print("Enter a valid input")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()