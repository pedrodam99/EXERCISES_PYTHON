n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

numbers = (n1, n2, n3, n4, n5)

pares = 0
impares = 0
positivos = 0
negativos = 0

#pares e impares
for n in numbers:
    if (n % 2 == 0):
        pares = pares + 1
    else:
        impares = impares + 1
        
#positivos e negativos
for n in numbers:
    if (n > 0):
        positivos = positivos + 1
    elif (n < 0):
        negativos = negativos + 1


        
print('%d valor(es) par(es)' %pares)
print('%d valor(es) impar(es)' %impares)
print('%d valor(es) positivo(s)' %positivos)
print('%d valor(es) negativo(s)' %negativos)

