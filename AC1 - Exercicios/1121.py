precoUnt = float(input())
qnt = int(input())

## calcular total
total = precoUnt * qnt

## calcular desconto
desc = 10
desc = 10 + qnt
descFinal = desc / 100

# calcular valor com desconto
valorFinal = total - (total * descFinal)
print('%.2f' %total)
print('%.2f' %valorFinal)
