# Lê massa e altura e calcula o IMC

massa, altura = input("Digite a massa seguida da altura: ").split()
#massa = float(massa)
#altura = float(altura)
massa, altura = float(massa), float(altura)

imc = massa / (altura ** 2)

print("IMC: {0:.2f}".format(imc))
