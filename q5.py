# lê um inteiro e imprime sua tabuada

numero = int(input("Digite um inteiro: "))

for i in range(1, 10 + 1):
    print("%d * %d = %d" % (numero, i, numero * i))
