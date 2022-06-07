qntTestes = int(input())

def getArrElements(n):
    elements = []
    cont = 0
    while (cont < qntTestes):
        n = int(input())
        elements.append(n)
        cont = cont + 1
    return elements
        
arrElements = getArrElements(qntTestes)


for n in arrElements:
    i = n
    arr = []
    while (i >= 1):
        if (n % i == 0):
            arr.append(i)
        i = i - 1

    if (len(arr) == 2 or n == 1):
        return print(f"{n} eh primo") 
    else:
        return print(f"{n} nao eh primo")
    

