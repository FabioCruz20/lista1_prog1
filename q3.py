# lê dois inteiros e imprime o resto da divisão do primeiro
# pelo segundo

a = int(input("Digite um numero inteiro: "))
b = int(input("Digite um numero inteiro: "))

resto = a % b

# %% é sequência de escape: ignora que o % é usado para formatar
# e imprime o caracter '%' propriamente dito
print("%d %% %d = %d" % (a, b, resto))


