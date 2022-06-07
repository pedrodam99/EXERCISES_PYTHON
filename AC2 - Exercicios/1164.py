qntLinhas = int(input())

alfabeto = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z'
    ]

i = 0
j = 1
k = 0
while (i < qntLinhas):
    print(alfabeto[i] * j)
    i += 1
    j += 1

