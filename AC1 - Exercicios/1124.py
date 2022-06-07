n = int(input())

if(n % 2 == 0):
    anterior = n - 1
    posterior = n + 2
else:
    anterior = n - 2
    posterior = n + 1


print(anterior, posterior)
