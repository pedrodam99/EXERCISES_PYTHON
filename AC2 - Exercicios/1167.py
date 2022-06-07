inicio = int(input())
fim = int(input())

i = inicio
qntBis = 0

while (i <= fim):
    if(i % 4 == 0 and i % 100 !=0 or i % 400 == 0):
            print(i)
            qntBis = qntBis + 1
    i += 1
print('bissextos: %d' %qntBis)
