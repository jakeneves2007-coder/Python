'''Programa que recebe uma string como entrada de usuário e imprime um dicionário contendo a quantidade de vezes que cada vogal do alfabeto aparece.

Exemplos:

aleluia -> {'a': 2, 'e': 1, 'i': 1, 'o': 0, 'u': 1}
bananeira -> {'a': 3, 'e': 1, 'i': 1, 'o': 0, 'u': 0}

'''

entrada = input("Digite uma string: ")
vogais = 'aeiou'
contador_vogais = {vogal: 0 for vogal in vogais}
for char in entrada:
    if char in contador_vogais:
        contador_vogais[char] += 1
print(contador_vogais)