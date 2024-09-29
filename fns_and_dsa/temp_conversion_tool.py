

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temprature = int(input("Enter the temperature to convert: "))
c_or_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if c_or_f == "f":
    print(f"{temprature}°F is {convert_to_celsius(temprature)}°C")
elif c_or_f == "c":
    print(f"{temprature}°C is {convert_to_fahrenheit(temprature)}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")
    
