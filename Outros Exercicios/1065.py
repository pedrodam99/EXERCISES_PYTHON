n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())


numbers = (n1, n2, n3, n4, n5)
i = 0

for n in numbers:
    if (n % 2 == 0):
        i = i + 1
print('%d valores pares' %i)
