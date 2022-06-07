valor = float(input(''))

#NOTAS
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

#MOEDAS
moeda_1 = resto_2 // 1
resto_1 = resto_2  % 1

moeda_050 = resto_1 // (50 / 100)
resto_050 = resto_1 % (50 / 100)

moeda_025 = resto_050 // (25/100)
resto_025 = resto_050 % (25/100)

moeda_010 = resto_025 // (10/100)
resto_010 = resto_025 % (10/100)

moeda_05 = resto_010 // (5/100)
resto_05 = resto_010 % (5/100)

moeda_01 = resto_05 // (1/100)
resto_01 = resto_05 % (1/100)



print('NOTAS:')
print('%d nota(s) de R$ 100.00' %notas_100)
print('%d nota(s) de R$ 50.00' %notas_50)
print('%d nota(s) de R$ 20.00' %notas_20)
print('%d nota(s) de R$ 10.00' %notas_10)
print('%d nota(s) de R$ 5.00' %notas_5)
print('%d nota(s) de R$ 2.00' %notas_2)

print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' %moeda_1)
print('%d moeda(s) de R$ 0.50' %moeda_050)
print('%d moeda(s) de R$ 0.25' %moeda_025)
print('%d moeda(s) de R$ 0.10' %moeda_010)
print('%d moeda(s) de R$ 0.05' %moeda_05)
print('%d moeda(s) de R$ 0.01' %moeda_01)

