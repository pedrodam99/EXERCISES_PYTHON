sal = float(input())

if (sal > 0 and sal <= 400):
    porcent = 15
    reajuste = sal * porcent / 100
    newSal = sal + reajuste

elif (sal > 400 and sal <= 800):
    porcent = 12
    reajuste = sal * porcent / 100
    newSal = sal + reajuste

elif (sal > 800 and sal <= 1200):
    porcent = 10
    reajuste = sal * porcent / 100
    newSal = sal + reajuste

elif (sal > 1200 and sal <= 2000): 
    porcent = 7
    reajuste = sal * porcent / 100
    newSal = sal + reajuste

else:
    porcent = 4
    reajuste = sal * porcent / 100
    newSal = sal + reajuste


print("Novo salario: %.2f" %newSal)
print("Reajuste ganho: %.2f" %reajuste)
print(f"Em percentual: {porcent} %")
