""" O alfabeto latino é composto por letras, começando em 'A' e encerrando em 'Z'. São vinte e seis caracteres diferentes, 
    se desconsiderarmos as acentuações e as diferenças entre letras maiúsculas e minúsculas.

    Harry, um garoto muito estudioso, percebeu que é possível inclusive desenhar usando letras. 
    Em um dos desenhos, Harry escreve na primeira linha e primeira coluna de uma folha quadriculada o primeiro caractere do alfabeto.
    Na segunda linha escreve duas vezes o segundo caractere, ocupando as duas primeiras colunas. 
    Na terceira linha escreve três vezes o terceiro caractere, ocupando as três primeiras colunas e assim por diante. 
    Harry percebeu que dessa forma consegue formar um triângulo alfabético, onde a primeira linha contém apenas um 'A' e a sétima contém sete 'G'. 


    Como Harry precisa estudar para realizar uma prova de programação (que para ele também é uma forma de magia!), pediu sua 
    ajuda para automatizar os desenhos dos "triângulos alfabéticos", criando um programa que receba como entrada um número 
    inteiro N (1 <= N <= 26) e que desenhe um triângulo com exatas N linhas, seguindo a mesma estratégia descrita no texto. Note 
    que o maior triângulo possível é aquele formado por vinte e seis linhas, onde na primeira linha há apenas um caractere 'A' e na
    última há somente vinte e seis caracteres 'Z'. """


N = int(input())
contador = 1
z = 0

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

while 1 <= contador <= N:
                                #Remove e devolve o item da lista solicitado
    quantidade_letra = contador * alfabeto.pop(z)
    print(quantidade_letra)
    
    contador += 1