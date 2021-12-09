def feet_to_inches(feet):
  return feet * 12

def hours_to_minutes(hours):
  return hours * 60

def celsius_to_fahrenheit(c):
  return (c * 9/5) + 32

print()

feet = float(input("Enter a length in feet: "))
inches = feet_to_inches(feet)
print(f"{feet} feet is {inches} inches.\n")

hours = float(input("Enter a duration in hours: "))
minutes = hours_to_minutes(hours)
print(f"{hours} hours is {minutes} minutes.\n")

c = float(input("Enter a temperature in Celsius: "))
f = celsius_to_fahrenheit(c)
print(f"{c} degrees Celsius is {f} degrees Fahrenheit.")
