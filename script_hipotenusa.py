#!/usr/bin/env python3

#Para rodar um script que receba input da linha de comando, devemos importar a função sys
import sys

#Para o cálculo do quadrado da hipotenusa, vamos receber os valores digitados na linha de comando usando sys.argv
valor1 = int(sys.argv[1])
valor2 = int(sys.argv[2])

#O script só será executado corretamente se os dois valores digitados forem números inteiros e maiores que zero
#Caso o usuário digite um número errado, mostraremos uma mensagem de erro
if isinstance(valor1, int) is False or valor1 <= 0 or valor1 >= 1000:
    print('Por favor, digite dois valores inteiros, positivos e menores que 1000')
elif isinstance(valor2, int) is False or valor2 <= 0 or valor2 >= 1000:
    print('Por favor, digite dois valores inteiros, positivos e menores que 1000')
else:
#O teorema de Pitágoras determina que o quadrado da hipotenusa de um triângulo retângulo é igual a soma dos quadrados de seus catetos
	qhip = (valor1**2)+(valor2**2)

#Podemos mostrar o resultado do cálculo em uma frase da seguinte maneira:
	print(f'O quadrado da hipotenusa para o triângulo retângulo com lados a={valor1} e b={valor2} é {qhip}')

