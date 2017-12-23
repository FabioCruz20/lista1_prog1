import math

base, altura = input("Digite a base seguida da altura: ").split()
base, altura = float(base), float(altura)
area_triangulo = (base * altura) / 2
print("Área do triângulo: {0:.2f}\n".format(area_triangulo))

lado = float(input("Digite a medida do lado do quadrado: "))
area_quadrado = lado * lado
print("Área do quadrado: {0:.2f}\n".format(area_quadrado))

raio = float(input("Digite a medida do raio do círculo: "))
area_circulo = math.pi * raio ** 2
print("Área do círculo: {0:.2f}\n".format(area_circulo))

base_maior = float(input("Digite a medida da base maior: "))
base_menor = float(input("Digite a medida da base menor: "))
altura_trapezio = float(input("Digite a altura do trapézio: "))
area_trapezio = ((base_maior + base_menor) * altura_trapezio) / 2
print("Área do trapézio: {0:.2f}\n".format(area_trapezio))

base_ret, altura_ret = input("Digite as medidas da base e da altura: ").split()
base_ret, altura_ret = float(base_ret), float(altura_ret)
area_retangulo = base_ret * altura_ret
print("Área do retângulo: {0:.2f}\n".format(area_retangulo))

diagonal_maior = float(input("Digite a medida da diagonal maior: "))
diagonal_menor = float(input("Digite a medida da diagonal menor: "))
area_losango = diagonal_maior * diagonal_menor / 2
print("Área do losango: {0:.2f}\n".format(area_losango))

