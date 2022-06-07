n = int(input())

if (n % 2 == 0):
    n = n - 1

i = 1
while (i <= n):
    if(i % 2 != 0):
        print(i)    
    i = i + 1
