qntAlunos = int(input())

notasOriginais = []
for i in range(qntAlunos):
    nota = float(input())
    notasOriginais.append(nota)

notasNovas = []
for i in range(qntAlunos):
    nota = float(input())
    notasNovas.append(nota)

listaIds = []
i = 1
while i <= qntAlunos:
    if i < 10:
        finalId = str(i)
        idAluno = f"00{i}"
        listaIds.append(idAluno)
    elif i < 100:
        finalId = str(i)
        idAluno = f"0{i}"
        listaIds.append(idAluno)
    elif i < 1000:
        finalId = str(i)
        idAluno = f"{i}"
        listaIds.append(idAluno)
    i += 1


todasNotas = list(zip(listaIds,notasOriginais, notasNovas))

def formatarNumero(numero):
    numero = str(numero)
    numero = numero.split(".")
    numeroInteiro = numero[0]
    if (numeroInteiro == "10"):
        numeroInteiro = f"{numeroInteiro}.00"
        return numeroInteiro
    else:
        numeroInteiro = f"0{numeroInteiro}.00"
        return numeroInteiro

notasAlteradas = 0
for notas in todasNotas:
    idAluno, notaOriginal, notaNova = notas
    if (notaNova == 10):
        if (notaOriginal == 10):
            notaFinal = 10.00
        else:
            notaFinal = notaOriginal + 2.00
            if (notaFinal > 10.00):
                notaFinal = 10.00
            notasAlteradas += 1

print(f"NOTAS ALTERADAS: {notasAlteradas}")
for notas in todasNotas:
    idAluno, notaOriginal, notaNova = notas
    if (notaNova == 10):
        if (notaOriginal == 10):
            notaFinal = 10.00
            notaOriginal = formatarNumero(notaOriginal)
            notaFinal = formatarNumero(notaFinal)
            print(f"-({idAluno}) original: {notaOriginal} | final: {notaFinal}")
        else:
            notaFinal = notaOriginal + 2.00
            if (notaFinal > 10.00):
                notaFinal = 10.00
            notaOriginal = formatarNumero(notaOriginal)
            notaFinal = formatarNumero(notaFinal)
            print(f"*({idAluno}) original: {notaOriginal} | final: {notaFinal}")
    else:
        notaFinal = notaOriginal
        notaOriginal = formatarNumero(notaOriginal)
        notaFinal = formatarNumero(notaFinal)
        print(f"-({idAluno}) original: {notaOriginal} | final: {notaFinal}")
