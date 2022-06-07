# Entrada de dados
cd1, n_pecas1, vlr_unt1 = input("").split()
cd2, n_pecas2, vlr_unt2 = input("").split()

#Convertendo dados
cd1 = int(cd1)
n_pecas1 = int(n_pecas1)
vlr_unt1 = float(vlr_unt1)

cd2 = int(cd2)
n_pecas2 = int(n_pecas2)
vlr_unt2 = float(vlr_unt2)

#Processamento de dados
item1 = n_pecas1 * vlr_unt1
item2 = n_pecas2 * vlr_unt2
resultado = item1 + item2


print('VALOR A PAGAR: R$ %.2f' %resultado)
