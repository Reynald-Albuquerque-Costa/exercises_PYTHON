""" Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", 
    indicando se os valores lidos são múltiplos entre si. """

A, B = input().split(" ") #Faz o usuário digitar os valores na mesma linha

A = int(A)
B = int(B)

if A % B == 0 or B % A == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')