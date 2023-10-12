""" Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno.
    Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela 
    mensagem "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for 
    inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, 
    o programa deve imprimir a mensagem "Aluno em exame.".

    No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a 
    mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média 
    anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou 
    "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) 
    apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno. """


N1, N2, N3, N4 = input().split(' ') #Faz o usuário digitar os valores na mesma linha

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

media_ponderada = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10

print(f'Media: {media_ponderada:.1f}')


if media_ponderada >= 7.0:
    print('Aluno aprovado.')
elif media_ponderada >= 5.0 and media_ponderada <= 6.9:
    print('Aluno em exame.')
    nota_exame = float(input())
    media_final = (nota_exame + media_ponderada) / 2
    print(f'Nota do exame: {nota_exame}')
    if media_final >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print(f'Media final: {media_final}')
else:
    print('Aluno reprovado.')