'''Escreva um programa que calcule a área total de um cilindro. O programa deve realizar as seguintes operações:

Recuperar, por meio da entrada de dados de usuário, os números inteiros do raio da base e da altura do cilindro; 
Calcular o valor da área total do cilindro;
Imprimir o valor resultante no terminal do usuário. 
Considere as seguintes informações para elaborar o seu programa:

area da BASE circular é igual a um circulo, ou seja, Ab = π * r^2, onde r é o raio da base do cilindro;

Area LATERAL é Al = 2 * π * r * h, onde r é o raio da base do cilindro e h é a altura do cilindro;

Area TOTAL é At = Ab + Al, onde Ab é a área da base e Al é a área lateral do cilindro.
'''

r = int(input("Valor do raio: "))
h = int(input("Valor da altura: "))
import math
Ab = math.pi * r ** 2

Al = 2 * math.pi * r * h

At =2*Ab + Al

print(f"A área total do cilindro é: {At:.2f}")