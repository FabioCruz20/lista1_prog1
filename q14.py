# Lê o salário base, o valor das vendas realizadas
# e calcula a comissão e o salário total
# comissão == 4% do valor das vendas

salario_base = float(input("Salário base: "))
valor_vendas = float(input("Valor obtido pelas vendas: "))

comissao = valor_vendas * 0.04
salario_total = salario_base + comissao
#salario_total = salario_base + (valor_vendas * 0.04)

print()
print("Salário base: %.2f" % (salario_base))
print("Comissão: {0:.2f}".format(comissao))
print("Salário total: {0:.2f}".format(salario_total))



