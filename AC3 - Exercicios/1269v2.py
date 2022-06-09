action = "0"
carrinho = [321, 12, 412, 2]
listaOutput = []

def exibir(lista):
    listaOutput.append(lista)

def adicionarOuRemover(lista, action, numero):
    if(action == "adicionar"):
        lista.append(numero)

while (action[0] != "encerrar"):
    action = input().split()
    if (action[0] == "exibir"):
        exibir(carrinho)
    elif(action[0] == "adicionar" or action[0] == "remover"):
        adicionarOuRemover(carrinho, action[0], action[1])



print(listaOutput)