# Lê duas notas com seus pesos e imprime a média ponderada

nota1 = float(input("Digite a nota: "))
peso1 = int(input("Digite o peso: "))

nota2, peso2 = input("Digite a nota seguida do peso: ").split()

nota2 = float(nota2)
peso2 = int(peso2)

#nota2 = float(input("Digite a nota: "))
#peso2 = int(input("Digite o peso: "))

media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

print("Média ponderada: %.3f" % (media))

