numeros = [1, 2, 4, 5, 7]
valor_de_busca = 6

for num in numeros:
    if num == valor_de_busca:
        print(f"O número {valor_de_busca} foi encontrado na lista.")
        break
    else:
        print(f"O número {valor_de_busca} não foi encontrado na lista.")
        
#O código acima verifica se o valor de busca (6) está presente na lista de números.
#O laço for percorre cada número na lista e compara com o valor de busca.
#Se o número for encontrado, uma mensagem é exibida e o laço é interrompido com a palavra-chave break.
<<<<<<< HEAD
#Se o número não for encontrado, o else é executado, mas isso acontece para cada número na lista, o que pode resultar em múltiplas mensagens de "não encontrado" até que o laço termine

'''if sheep_counter >= 120:
    make_a_bed()
    take_a_shower()
    sleep_and_dream()
feed_the_sheepdogs()'''

#Alimentar os cães pastores, no entanto, é sempre feito (ou seja, a função feed_the_sheepdogs() não é recuada e não pertence ao bloco if, o que significa que é sempre executado.)
 
=======
#Se o número não for encontrado, o else é executado, mas isso acontece para cada número na lista, o que pode resultar em múltiplas mensagens de "não encontrado" até que o laço termine
>>>>>>> d9bb805b2a3bf47831045b94994c84ce3eaddebd
