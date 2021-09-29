#!/usr/bin/env python3

#Para rodar um script que receba input da linha de comando, devemos importar a função sys
import sys

#Para o cálculo do quadrado da hipotenusa, vamos receber os valores digitados na linha de comando usando sys.argv
valor1 = sys.argv[1]
valor2 = sys.argv[2]

#O script só será executado corretamente se os dois valores digitados forem números inteiros e maiores que zero
#Caso o usuário digite um número errado, mostraremos uma mensagem de erro
#A checagem será feita através da função is_integer

def is_integer(n):
	try:
		float(n)
	except ValueError:
		return False
	else:
		return float(n).is_integer()

if is_integer(valor1) is False or is_integer(valor2) is False:
	print('Por favor, digite dois valores inteiros, positivos e menores que 1000')

#Para checar se os valores inseridos são maiores que zero e menores que 1000, definimos as variáveis como int para comparação
else:
	valor1 = int(valor1)
	valor2 = int(valor2)
	if valor1 <= 0 or valor2 <= 0 or valor1 >= 1000 or valor2 >= 1000:
		print('Por favor, digite dois valores inteiros, positivos e menores que 1000')
	else:
#O teorema de Pitágoras determina que o quadrado da hipotenusa de um triângulo retângulo é igual a soma dos quadrados de seus catetos
		qhip = (valor1**2)+(valor2**2)

#Podemos mostrar o resultado do cálculo em uma frase da seguinte maneira:
		print(f'O quadrado da hipotenusa para o triângulo retângulo com lados a={valor1} e b={valor2} é {qhip}')

