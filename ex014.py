""" Ao perceber que um de seus amigos estava com dificuldades financeiras, Victória, uma garota muito inteligente, decidiu 
    ajudá-lo com uma "vaquinha digital", em que todos poderiam doar quanto pudessem para ajudar seu amigo.
     
    Para isso, Victória criou uma criptomoeda, a Vic Coin, em que cada unidade equivale à R$ 2,50. Assim, os doadores 
    primeiro compram a criptomoeda e, em seguida, depositam uma parte delas para doação. A parte que não foi doada pode ficar
    guardada em uma carteira digital e poderá ser usada no futuro para outras doações. Genial! 
    
    Victória está ocupada implementando o que é necessário para o funcionamento do ambiente de doações, por isso pediu para
    que você a ajudasse com uma das partes essenciais: a contabilização de doações e a conversão para reais.
    
    Seu objetivo é criar um programa que receba como entrada diversas doações feitas em Vic Coin e, ao final, exiba o total
    de doações em Vic Coin (VC$) e o mesmo valor convertido para reais (R$). """


vic_coin = 0.0
acumulador = 0.0

while vic_coin != -1.0:
    vic_coin = float(input())
    #Guarda e soma na variável acumulador os vic coins
    acumulador += vic_coin

acumulador += 1.0
conversao_para_real = acumulador * 2.50 

print(f'VC$ {acumulador:.2f}')
print(f'R$ {conversao_para_real:.2f}')