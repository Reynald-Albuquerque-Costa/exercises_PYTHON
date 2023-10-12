""" Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) 
    e o total de combustível gasto (em litros). """

X = int(input())
Y = float(input())

consumo_medio = X / Y

print(f'{consumo_medio:.3f} km/l')