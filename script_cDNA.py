#!/usr/bin/env python3
import sys

#Com a função sys.argv, o script receberá o input da linha de comando
#O primeiro argumento se refere à sequência do gene de interesse
seq = str(sys.argv[1])
#O segundo e terceiro se referem às posições de início e término do primeiro CDS
n1 = int(sys.argv[2])
n2 = int(sys.argv[3])
#O terceiro e quarto se referem às posições de início de término do segundo CDS
n3 = int(sys.argv[4])
n4 = int(sys.argv[5])

#Conferido se os argumentos inseridos são válidos:
if isinstance(seq, str) is False:
    print('Por favor, insira uma sequência de DNA válida, contendo somente bases A, T, G e C')
elif isinstance(n1, int) is False or isinstance(n2, int) is False or isinstance(n3, int) is False or isinstance(n4, int) is False:
    print('Por favor, insira números inteiros que correspondam ao início e fim da sua sequência de interesse')
elif n1 > len(seq) or n2 > len(seq) or n3 > len(seq) or n4 > len(seq):
    print('Os números inseridos não podem ser maiores do que o comprimento da sequência de DNA inserida')
elif n1 <=0 or n2 <=0 or n3 <= 0 or n4 <= 0:
    print('Os números inseridos não podem ser negativos ou iguais a zero')
else:
#Determinando a sequência da primeira CDS com base nos dados inseridos:
    cds1 = seq[(n1-1):n2]
    if cds1.find('ATG') == 0:
        print(f'A primeira sequência se inicia na posição {n1} com o códon ATG')
    else:
        print(f'A primeira sequência que se inicia na posição {n1} não começa com o códon ATG')
#Determinando a sequência da segunda CDS com base nos dados inseridos:
    cds2 = seq[(n3 - 1):n4]
    if cds2.find('TAG') == (len(cds2)-3):
        print(f'A segunda sequência termina na posição {n4} e suas três últimas bases formam o códon TAG')
    elif cds2.find('TAA') == (len(cds2) - 3):
        print(f'A segunda sequência termina na posição {n4} e suas três últimas bases formam o códon TAA')
    elif cds2.find('TGA') == (len(cds2)-3):
        print(f'A segunda sequência termina na posição {n4} e suas três últimas bases formam o códon TGA')
    else:
        print(f'A segunda sequência termina na posição {n4} e suas três últimas bases não formam nenhum códon de parada')
#Caso a primeira sequência comece com ATG e a segunda termine com um dos códons de parada, faremos a concatenação de ambas:
    if cds1.find('ATG') == 0:
        if cds2.find('TAG') == (len(cds2)-3) or cds2.find('TAA') == (len(cds2) - 3) or cds2.find('TGA') == (len(cds2)-3):
        	concat = cds1 + cds2
        print(f'As regiões codificantes CDS1 e CDS2 formam a seguinte sequência de bases: {concat}')
