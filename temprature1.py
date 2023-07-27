def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("***TEMPERATURE CONVERTER***")
temperature = float(input("Enter the temperature: "))
print("Select your temperature unit")
print("1. Celsius")
print("2. Fahrenheit")

while True:

    unit = input("Enter the unit (1,2): ")

    if unit == "1":
        fahrenheit = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C = {fahrenheit}°F")
        break

    elif unit == "2":
        celsius = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F = {celsius}°C")
        break


else:
    print("Invalid unit entered. plz enter valid unit!!!!")
