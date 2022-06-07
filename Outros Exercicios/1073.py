n = int(input())

if(n % 2 != 0):
    n = n - 1
    
i = 0
x = 2

while (i < (n/2)):
    i = i + 1
    #outro while
    while(x <= n):
        resultado = x ** 2
        print('%d ^ 2 = %d' %(x, resultado))
        x = x + 2
    
