acumulador = 0
p = 0

for x in range(6):
    n = float(input())
    if (n > 0):
        acumulador = acumulador + n
        p = p + 1
media = acumulador / p

print('%d valores positivos' %p)
print('%.1f' %media)
