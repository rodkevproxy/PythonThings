

unit = input("Is the unit in Celsius or Fahrenheit (C/F)")

temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 32, 1)
    print (f"The temperature in fahrenheit is {temp}")
elif unit == "F": 
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsious is {temp}")
else: 
    print(f"Unit {unit} is invalid")

