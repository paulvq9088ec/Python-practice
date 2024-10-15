#Solicitar el valor del radio de un círculo para calcular el área

from math import pi
r = float(input('Ingresa el valor del radio: '))
area = round((pi * r ** 2),2)
print(f'El área del círculo es de: {area}')