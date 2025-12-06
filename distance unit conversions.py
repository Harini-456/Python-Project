a = input("Enter the unit want to convert from (km,m,cm,mm): ")
b = input("Enter the unit want to convert to (km,m,cm,mm): ")
c = int(input("Enter value: "))

if a == 'km' and b == 'm':
    ans = c*1000
elif a == 'km' and b == 'cm':
    ans  = c*100000
elif a == 'km' and b == 'mm':
    ans = c * 1000000
elif a == 'm' and b == 'km':
    ans = c/1000
elif a == 'm' and b == 'cm':
    ans = c*100
elif a == 'm' and b == 'mm':
    ans = c*1000
elif a == 'cm' and b == 'km':
    ans = c/100000
elif a == 'cm' and b == 'm':
    ans = c/100
elif a == 'cm' and b == 'mm':
    ans = c*10
elif a == 'mm' and b == 'km':
    ans = c/1000000
elif a == 'mm' and b == 'm':
    ans = c/1000
elif a == 'mm' and b == 'cm':
    ans = c/10

print("The conversion from ",a,"to ",b,"for no ",c,"is: ",ans)