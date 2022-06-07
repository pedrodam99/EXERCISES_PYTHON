valor = int(input())

lista = []

while(valor >= 1):
    lista.append(valor)
    valor -= 1

acc = 1

for n in lista:
    acc *= n
print(acc)
