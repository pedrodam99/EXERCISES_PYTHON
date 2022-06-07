number, i, multiplicador = input('').split()

number = int(number)
multiplicador = int(multiplicador)
i = int(i)

while(i <= multiplicador):
    resultado = i * number
    print("%d X %d = %d" %(i, number, resultado))
    i = i + 1
