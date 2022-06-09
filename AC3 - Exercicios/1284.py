# qntAlunos = int(input())

# notasOriginais = []
# for i in range(qntAlunos):
#     nota = float(input())
#     notasOriginais.append(nota)

# notasNovas = []
# for i in range(qntAlunos):
#     nota = float(input())
#     notasNovas.append(nota)

# todasNotas = list(zip(notasOriginais, notasNovas))

# notasAlteradas = 0
# for notas in todasNotas:
#     notaOriginal, notaNova = notas
#     if (notaNova == 10):
#         if (notaOriginal == 10):
#             notaFinal = 10.00
#             print(f"-(XXX) original: {notaOriginal:.2f} | final: {notaFinal}")
#         else:
#             notaFinal = notaOriginal + 2.00
#             if (notaFinal > 10.00):
#                 notaFinal = 10.00
#             print(f"*(XXX) original: {notaOriginal:.2f} | final: {notaFinal}")
#             notasAlteradas += 1
# print(notasAlteradas)


#FAZENDO ID DOS ALUNOS
qntAlunos = int(input())
i = 1
while (i < qntAlunos):
    i = str(i)
    
