x = int(input())
y = int(input())

acc = 0
x = x - 1

while (x > y):
    if (x % 2 != 0):
        acc = acc + x
    x = x - 1
print(acc)
