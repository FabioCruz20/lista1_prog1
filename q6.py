import math

# lê um raio e imprime o volume da esfera que tem esse raio

raio = int(input("Digite um inteiro: "))

volume = (4 * math.pi * raio**3)/3
print("Volume da esfera = %f metros cúbicos" % (volume))
