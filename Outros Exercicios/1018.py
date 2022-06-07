valor = int(input(''))

notas_100 = valor // 100
resto_100 = valor % 100

notas_50 = resto_100 // 50
resto_50 = resto_100 % 50

notas_20 = resto_50 // 20
resto_20 = resto_50 % 20

notas_10 = resto_20 // 10
resto_10 = resto_20 % 10

notas_5 = resto_10 // 5
resto_5 = resto_10 % 5

notas_2 = resto_5 // 2
resto_2 = resto_5 % 2

notas_1 = resto_2

print(valor)
print('%d Nota(s) de R$ 100,00' %notas_100)
print('%d Nota(s) de R$ 50,00' %notas_50)
print('%d Nota(s) de R$ 20,00' %notas_20)
print('%d Nota(s) de R$ 10,00' %notas_10)
print('%d Nota(s) de R$ 5,00' %notas_5)
print('%d Nota(s) de R$ 2,00' %notas_2)
print('%d Nota(s) de R$ 1,00' %notas_1)
