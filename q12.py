

deposito = float(input("Digite o valor do depósito: "))
taxa_juros = float(input("Digite a taxa de juros: "))
tempo_aplicacao = int(input("Digite o tempo de aplicação em meses: "))

juros = deposito * taxa_juros * tempo_aplicacao

montante_final = deposito + juros

print("Montante final: {0:.2f}".format(montante_final))
