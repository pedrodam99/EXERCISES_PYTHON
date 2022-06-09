segs = 0
lista = []
acc = 0

#add segundos dentro de uma lista
while (segs >= 0):
    segs = int(input())
    if (segs >= 0):
        lista.append(segs)

#somando segundos
for n in lista:
    acc = acc + n

#calculando media
media = acc / len(lista)

#exibindo resultados
print(f"MEDIA: {media:.2f}")

for n in lista:
    print(n)