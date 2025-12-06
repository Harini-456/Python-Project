p = int(input("Enter the Principle: "))
r = int(input("Enter the Rate of Interest: "))
t = int(input("Enter the Time period: "))
n = int(input("Enter the Number of times interest is compounded per year: "))

si = (p*r*t)/100
ci = p *( (1+r/(100*n)) ** (n*t) )- p

print("Simple Interest: ",si)
print("Compound Interest: ",ci)