a = int(input("Enter year: "))

if( a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print("The year",a,"is leap year")
else:
    print("The year",a,"is not leap year")