inicio = int(input())
fim = int(input())

arrElementos = []
arrPrimos = []

# colocando todos elementos na lista
while (inicio <= fim):
    arrElementos.append(inicio)
    inicio += 1

# verificando quais são primos e colocando numa lista só com primos

for n in arrElementos:
    i = n
    arr = []
    while (i >= 1):
        if (n % i == 0):
            arr.append(i)
        i = i - 1
    if (len(arr) == 2):
        arrPrimos.append(n)

qntPrimos = len(arrPrimos)
# saida dos dados
j = 0
for n in arrPrimos:
    print(arrPrimos[j])
    j += 1

print(f"primos: {qntPrimos}")
