n1 = float(input())
i = 1
if (n1 >= 0):
    acc = n1
    while (n1 >= 0):
        n1 = float(input())
        if (n1 >= 0):
            acc = acc + n1
            i = i + 1
    media = acc / i
    print('%.2f' %media)
