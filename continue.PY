numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = []

for num in numeros:
    if num % 2 != 0:
        continue
    numeros_pares.append(num)
print(f"Os números pares são: \n{numeros_pares}")

#O laço for percorre cada número na lista "numeros".
#Dentro do laço, há uma condição que verifica se o número é ímpar (num % 2 != 0).
#Se a condição for verdadeira, a palavra-chave continue é usada para pular o restante do código dentro do laço para aquele número específico e passar para a próxima iteração.
#Se o número for par, ele é adicionado à lista "numeros_pares".
#No final, o programa imprime a lista de números pares encontrados.
#Se o numero for ímpar, ele não será adicionado à lista e o laço continuará para o próximo número sem executar o código que adiciona o número à lista.