a, b, c = input('').split()

a = float(a)
b = float(b)
c = float(c)

area_trapezio = ((a + b)  * c) / 2
per_triangulo = a + b + c

if ((b - c) < a and a < (b + c)):
    if((a - c) < b and b < (a + c)):
        if((a - b) < c and c <(a + b)):
            print('Perimetro = %.1f' %per_triangulo)
else:
    print('Area = %.1f' %area_trapezio)

