n1, n2, n3 = input().split()

# tratando dados
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

# ordenando lados
lados = [n1, n2, n3]
lados = sorted(lados, reverse = True)

a = lados[0]
b = lados[1]
c = lados[2]

# criando flags booleanas

tri_retangulo = (a ** 2) == (b ** 2) + (c ** 2)
tri_obtusangulo = (a ** 2) > (b ** 2) + (c ** 2)
tri_acutangulo = (a ** 2) < (b ** 2) + (c ** 2)
tri_equilatero = a == b and b == c and b == c
tri_isosceles = a == b != c or a == c != b or b == c != a
nao_forma_tri = a >= b + c


# determinando o tipo do triangulo

if(nao_forma_tri):
   print('NAO FORMA TRIANGULO')
else:
  if (tri_retangulo):
    print('TRIANGULO RETANGULO')

  if (tri_obtusangulo):
    print('TRIANGULO OBTUSANGULO')

  if (tri_acutangulo):
    print('TRIANGULO ACUTANGULO')

  if (tri_equilatero):
    print('TRIANGULO EQUILATERO')

  if (tri_isosceles):
    print('TRIANGULO ISOSCELES')

 





