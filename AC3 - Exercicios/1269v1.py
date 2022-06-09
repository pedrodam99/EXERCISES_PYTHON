carrinho = []
carrinho.append((input().split()))
listaAux = carrinho[0]
carrinho = []

for element in listaAux:
    carrinho.append(int(element))

action = [0]

def exibir(lista):
    lista = sorted(lista)
    for elem in lista:
        print(elem, end=" ")
    print("")

def adicionarOuRemover(lista, action, numero):
    if(action == "adicionar"):
        lista.append(numero)
    elif(action == "remover"):
        if(lista.count(numero) == 0):
            print(f"código {numero} não encontrado")
        else:
            lista.remove(numero)

while (action[0] != "encerrar"):
    action = input().split()
    if (action[0] == "exibir"):
        exibir(carrinho)
    elif(action[0] == "adicionar" or action[0] == "remover"):
        action[1] = int(action[1])
        adicionarOuRemover(carrinho, action[0], action[1])
exibir(carrinho)


