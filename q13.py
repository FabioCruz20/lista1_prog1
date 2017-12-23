# Lê o salário do funcionário e o valor do salário mínimo
# e imprime a quantidade de salários mínimos que o funcionário
# recebe

salario_funcionario = float(input("Salário do funcionário: "))
salario_minimo = float(input("Salário mínimo: "))

quant_salarios = salario_funcionario / salario_minimo

print("O funcionário recebe {0:.2f} salário(s) mínimo(s)".format(quant_salarios))

