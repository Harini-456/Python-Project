a = input("Enter the unit want to convert from (celsius, fahrenheit, kelvin): ")
b = input("Enter the unit want to convert to (celsius, fahrenheit, kelvin): ")
c = float(input("Enter value: "))

if a == 'celsius' and b == 'fahrenheit':
    ans = (c*1.8)+32
elif a == 'celsius' and b == 'kelvin':
    ans = c + 273.15
elif a == 'fahrenheit' and b == 'celsius':
    ans = (c - 32) / 1.8
elif a == 'fahrenheit' and b == 'kelvin':
    ans = 273.5 + ((c - 32.0) * (5.0/9.0))
elif a == 'kelvin' and b == 'celsius':
    ans = c - 273.15
elif a == 'kelvin' and b == 'fahrenheit':
    ans = (c - 273.15) * 1.8  + 32

print("The conversion from ",a,"to ",b,"for no ",c,"is: ",ans)