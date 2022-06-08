qntCanais = int(input())

listaCanais = []
i = 0

#criando a lista de canais
while (i < qntCanais):
    nome, subs, monetizacao, ehPremium = input().split(";")  
    #tratando dados
    nome = str(nome)
    subs = int(subs)
    monetizacao = float(monetizacao)
    ehPremium = str(ehPremium)
    #add canal na lista
    canal  = [nome, subs, monetizacao, ehPremium]
    listaCanais.append(canal)
    i += 1

dinheiroPremium = float(input())
dinheiroNaoPremium = float(input())

#Funcao para calcular monetizacao do canal
def calcularLucro(subs, monetizacao, ehPremium):
    if (ehPremium == "sim"):
       lucroFinal = (subs // 1000 * dinheiroPremium) + monetizacao 
       return lucroFinal
    else:
        lucroFinal = (subs // 1000 * dinheiroNaoPremium) + monetizacao
        return lucroFinal

#Output do Exercicio
print("-" * 5)
print("BÔNUS")
print("-" * 5)

for canal in listaCanais:
    lucro = calcularLucro(canal[1], canal[2], canal[3])
    print(f"{canal[0]}: R$ {lucro:.2f}")
    
        

