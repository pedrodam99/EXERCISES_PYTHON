doacao = 0
saldoVC = 0

while (doacao != -1.00):
    saldoVC = saldoVC + doacao
    doacao = float(input())


#converter e imprimir
saldoReais = saldoVC * 2.5

print(f"VC$ {saldoVC:.2f}")
print(f"R$ {saldoReais:.2f}")
