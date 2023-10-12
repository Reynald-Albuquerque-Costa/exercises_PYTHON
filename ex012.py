""" Sua tarefa é construir um programa que receba como entrada um número natural N (0 <= N <= 10)
    e exibir a tabuada de N de 1 até 10. """

N = int(input())
contador = 1

while 0 <= contador <= 10:
    tabuada = N * contador
    print(f'{N} x {contador} = {tabuada}')
    contador += 1