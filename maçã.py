'''Receba o número inteiro n da quantidade inicial de maçãs na mochila;
Receba um valor que indica se você ou o seu amigo irão retirar a primeira maçã;

Se você vencer, o programa deverá imprimir na tela a frase: “Parabéns! Você venceu o jogo!”;

Se o seu amigo vencer, o programa deverá imprimir na tela a frase: “Que pena! Você perdeu o jogo!”'''

n = int(input("Digite a quantidade inicial de maçãs na mochila: "))
primeira_maçã = input("Digite 'eu' se você irá retirar a primeira maçã ou 'amigo' se seu amigo irá retirar a primeira maçã: ")


if primeira_maçã == "eu":
    if n % 2 == 0:
        print("Que pena! Você perdeu o jogo!")
        
if primeira_maçã == "eu":
    if n % 2 != 0:
        print("Parabéns! Você venceu o jogo!")
        
if primeira_maçã == "amigo":
    if n % 2 == 0:
        print("Parabéns! Você venceu o jogo!")
             
if primeira_maçã == "amigo":
    if n % 2 != 0:
        print("Que pena! Você perdeu o jogo!")
        