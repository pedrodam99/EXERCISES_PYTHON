a, b, c = input('').split()

#transformo os dados
a = float(a)
b = float(b)
c = float(c)

#validações

if a == 0:
    print('Impossivel calcular')
else:
    delta = (b ** 2) -4 * a * c
    raiz = delta ** 0.5
    if (raiz >= 0):
        r1 = (-b + (raiz)) / (2 * a)
        r2 = (-b - (raiz)) / (2 * a)
        print('R1 = %.5f' %r1)
        print('R2 = %.5f' %r2)
    else:
        print('Impossivel calcular')
        
    



