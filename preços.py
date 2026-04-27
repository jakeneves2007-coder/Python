# -*- coding: utf-8 -*-

'''Faça um laço de repetição (for ou while) para percorrer a lista e recuperar o valor do total de preços;
Calcule a média aritmética dos preços;
Imprima o valor da média no terminal. 
Após completar o código fonte, marque as alternativas corretas sobre o programa.'''



import random
import math

# Aqui está a lista de preços
precos_lista = [2.50, 5.99, 1.20, 10.00, 4.35, random.uniform(0.1, 5.0)]

# Aqui está a variável que armazenará a soma dos preços
total_soma = sum(precos_lista)

while True:
    for preço in precos_lista:
        media = total_soma / len(precos_lista)
    print(f"A média dos preços é: ({math.floor(media):.2f})")
    break
#math.floor() é usado para arredondar o valor da média para baixo, garantindo que seja um número inteiro. O resultado é formatado para exibir duas casas decimais usando :.2f.