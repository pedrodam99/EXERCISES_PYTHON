n_entries = int(input())

i = 1
dentro = 0
fora = 0

while (i <= n_entries):
    i = i + 1
    n = int(input())
    if(n >= 10 and n <= 20):
        dentro = dentro + 1
    else:
        fora = fora + 1
print('%d in' %dentro)
print('%d out' %fora)
    
