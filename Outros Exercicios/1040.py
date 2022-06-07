n1, n2, n3, n4 = input().split()

#tratamento de dados
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

#processamento
p1 = 2
p2 = 3
p3 = 4
p4 = 1
nota_pond = (n1 * p1) + (n2 * p2) + (n3 * p3) + (n4 * p4)
total_pesos = 10

media = nota_pond / total_pesos

#verificações e exibição


if media >= 7:
    print('Media: %.1f' %media)
    print('Aluno aprovado.')
elif media < 5:
    print('Media: %.1f' %media)
    print('Aluno reprovado.')
else:
    nota_exame = input('')
    nota_exame = float(nota_exame)
    media_exame = (media + nota_exame) / 2
    if media_exame > 5:
        print('Media: %.1f' %media)
        print('Aluno em exame.')
        print('Nota do exame: %.1f' %nota_exame)
        print('Aluno Aprovado.')
        print('Media final: %.1f' %media_exame)
        
    else:
        print('Media: %.1f' %media)
        print('Aluno em exame.')
        print('Nota do exame: %.1f' %nota_exame)
        print('Aluno reprovado.')
        print('Media final: %.1f' %media_exame)
        
    
