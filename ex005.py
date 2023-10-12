""" Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
    a) a área do triângulo retângulo que tem A por base e C por altura.
    b) a área do círculo de raio C. (pi = 3.14159)
    c) a área do trapézio que tem A e B por bases e C por altura.
    d) a área do quadrado que tem lado B.
    e) a área do retângulo que tem lados A e B. """

A, B, C = input().split(" ") #Faz o usuário digitar os três valores na mesma linha

A = float(A)
B = float(B)
C = float(C)

pi = 3.14159

triangulo = (A*C) / 2
circulo = pi * (C ** 2)
trapezio = ((A + B) * C) / 2
quadrado = B * B
retangulo = A * B

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')