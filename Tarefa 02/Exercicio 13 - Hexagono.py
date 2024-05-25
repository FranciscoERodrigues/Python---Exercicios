#Curso Basico de Python
#Nome do Desenvolvedor: Francisco Emerson Rogerio Rodrigues
#Versao 1.0
#Exercicio de Logica de Programação
#com a logica de Programação Python
#exercicio 13 - Hexagono

import math

lado = float(input("digite o valor do lado do hexagono:"))
resultado = (3*math.pow(lado,2)*math.sqrt(3)/2)
print(" A area do hexagono é",round (resultado,2), "m²")
