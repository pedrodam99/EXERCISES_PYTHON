inicio, fim = input().split()

# tratando dados

inicio = int(inicio)
fim = int(fim)

if (inicio > fim):
    resultado = (24 - inicio) + fim
    print(f"O JOGO DUROU {resultado} HORA(S)")

elif (fim > inicio):
    resultado = (24 - inicio) + fim
    resultado = resultado % 24
    print(f"O JOGO DUROU {resultado} HORA(S)")
else:
    resultado = 24
    print(f"O JOGO DUROU {resultado} HORA(S)")
    
