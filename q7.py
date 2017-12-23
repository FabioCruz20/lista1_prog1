# lê um valor em polegadas e imprime o correspondente em cm

# polegadas     cm
#         1     1 * 2.54 = 2.54 cm
#         2     2 * 2.54 = 5.08 cm
#         3     3 * 2.54 = 7.62 cm
    
polegadas = float(input("Digite um numero real: "))
centimetros = polegadas * 2.54

print("%f\" = %f cm" % (polegadas, centimetros))
