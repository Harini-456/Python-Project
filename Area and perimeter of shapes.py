shape = input("Enter a shape: ")

if shape == 'square':
    val = int(input("Enter side: "))
    a = val * val
    p = 4 * val
    print("Area of square is: ",a)
    print("Perimeter of square is: ",p)

elif shape == 'rectangle':
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    a = l * b
    p = 2 * (l + b)
    print("Area of rectangle is: ",a)
    print("Perimeter of rectangle is: ",p)

elif shape == 'triangle':
    base = int(input("Enter base: "))
    hei = int(input("Enter height: "))
    s1 = float(input("Enter side 1: "))
    s2 = float(input("Enter side 2: "))
    s3 = float(input("Enter side 3: "))
    a = 0.5 * base * hei
    p = s1+s2+s3
    print("Area of triangle is: ",a)
    print("Perimeter of triangle is: ",p)

elif shape == 'circle':
    r = int(input("Enter radius: "))
    a = 3.14 * (r ** 2)
    c = 2 * 3.14 * r
    print("Area of circle is: ",a)
    print("Circumference of circle is: ",c)

elif shape == 'parallelogram':
    base = int(input("Enter base: "))
    hei = int(input("Enter height: "))
    a = base * hei
    s1 = float(input("Enter side 1: "))
    s2 = float(input("Enter side 2: "))
    p = 2 * (s1 + s2)
    print("Area of parallelogram is: ",a)
    print("Perimeter of parallelogram is: ",p)

elif shape == 'trapezium':
    base1 = float(input("Enter base 1 value: "))
    base2 = float(input("Enter base 2 value: "))
    hei = float(input("Enter height:"))
    s1 = float(input("Enter side 1: "))
    s2 = float(input("Enter side 2: "))
    s3 = float(input("Enter side 3: "))
    s4 = float(input("Enter side 4: "))
    area = 0.5 * (base1 + base2) * hei
    perimeter = s1 + s2 + s3 + s4

    print("Area of trapezium is: ",area)
    print("Perimeter of trapezium is: ",perimeter)