FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    # Takes temperature in fahrenheit and converts to celsius
    temperature = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}\u00b0F is {temperature}\u00b0C")

def convert_to_fahrenheit(celsius):
    # Takes temperature in celsius and converts to fahrenheit
    temperature = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}\u00b0C is {temperature}\u00b0F")

def main():
    try:
        temperature_input = float(input("Enter the temperature to convert: "))
        temperature_format = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        if temperature_format == "C":
            convert_to_fahrenheit(temperature_input)
        elif temperature_format == "F":
            convert_to_celsius(temperature_input)
        else:
            print("Enter a valid input")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()