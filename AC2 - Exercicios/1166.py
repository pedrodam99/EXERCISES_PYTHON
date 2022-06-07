valorDivida = int(input())
valorMes = int(input())

i = 1

while (valorDivida > 0):
    print("pagamento: %d" %i)
    print("antes = %d" %valorDivida)
    valorDivida = valorDivida - valorMes
    if(valorDivida <= 0):
        valorDivida = 0
    print("depois = %d" %valorDivida)
    print("-----")
    i += 1
