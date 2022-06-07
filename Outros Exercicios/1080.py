arr = []
for x in range(100):
    n = int(input())
    arr.append(n)

maior = max(arr)
indice_maior = arr.index(max(arr)) + 1

print(maior)
print(indice_maior)
