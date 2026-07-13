# Convert temperature from Celsius to Fahrenheit and vice versa

celsius=30
print("Temperature Converter")
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} C = {fahrenheit} F ")
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} F = {celsius} C ")

# Is it a hot day 

print("Hot day : " , celsius > 30)
print("Hot day" if celsius > 30 else "Not a hot day")