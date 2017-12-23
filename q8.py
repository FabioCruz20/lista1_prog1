import math

altura = float(input("Digite a altura: "))
raio = float(input("Digite o raio: "))

area_circulos = 2 * math.pi * raio ** 2
area_lateral = (2 * math.pi * raio) * altura

area_cilindro = area_circulos + area_lateral

quant_latas = area_cilindro / 15
custo = quant_latas * 50.00

print("Área: %.2f" % area_cilindro)
print("%f latas pintam %f metros quadrados" % (quant_latas, quant_latas * 15))
print("Latas usadas: %d" % quant_latas)
print("Custo: R$ %.2f" % custo)

