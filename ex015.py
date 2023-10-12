""" Você sabe o que são anos bissextos? Resumidamente, em anos bissextos o mês de fevereiro é mais extenso, contendo 29 dias,
    ao invés de apenas 28. O cálculo para descobrir se um ano é bissexto também é bastante simples, pois um ano é bissexto se
    é divisível por 4 e não por 100, ou se é divisível por 400. 
    
    Claudia adora anos bissextos, porque ela nasceu em um! Mais precisamente, Claudia nasceu no dia 29 de fevereiro, por isso
    sente que seu aniversário só ocorre "de verdade" nos anos que são bissextos, afinal pode projetar a festa sem ter que explicar
    aos amigos se comemorará no dia 28 de fevereiro ou no dia 01 de março.
    
    Você foi convidado para a comemoração de Claudia, mas para isso ela pediu um presente especial, solicitou que você construa
    um programa que a ajude a ficar menos ansiosa para saber quais são os anos em que ela poderá realizar festas na data correta.
    Para isso, seu programa deverá receber um ano INÍCIO e um ano FIM e exibir todos os anos bissextos do intervalo fechado [ INÍCIO..FIM ].
    Ao final, o programa também deve exibir a quantidade de anos bissextos do intervalo. """


INÍCIO  = int(input())
FIM = int(input())

acumulador = 0
 
while INÍCIO <= FIM:
    if INÍCIO % 4 == 0 and INÍCIO % 100 != 0 or INÍCIO % 400 == 0:
        print(INÍCIO)
        #Totaliza os anos bissextos e guarda na variável
        acumulador += 1
    INÍCIO += 1
 

print(f'bissextos: {acumulador}')