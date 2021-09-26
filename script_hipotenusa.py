#!/usr/bin/env python3

#Para rodar um script que receba input da linha de comando, devemos importar a função sys
import sys

#Para o cálculo do quadrado da hipotenusa, vamos receber os valores digitados na linha de comando usando sys.argv
valor1 = sys.argv[1]
valor2 = sys.argv[2]

#O teorema de Pitágoras determina que o quadrado da hipotenusa de um triângulo retângulo é igual a soma dos quadrados de seus catetos

qhip = (valor1**2)+(valoe2**2)

#Podemos mostrar o resultado do cálculo em uma frase da seguinte maneira:
print(f'O quadrado da hipotenusa para o triângulo retângulo com lados a={valor1} e b={valor2} é {qhip}')

