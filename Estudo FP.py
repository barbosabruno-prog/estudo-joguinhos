#Teorema de Pitágoras

import math

print('*****Cálculo da Hipotenusa*****')

a, b = input('Digite os voalores dos catetos, separados por espaço: ').split()

a = int(a)
b = int(b)

hip = math.sqrt(pow(a,2) + pow(b, 2))

print('A hipotenusa do triângulo com lados {} e {} é {}.'.format(a, b, hip))

