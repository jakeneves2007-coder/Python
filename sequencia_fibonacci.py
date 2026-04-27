<<<<<<< HEAD
'''Programa que imprima a soma dos n primeiros números da sequência de fibonacci. Escreva o valor numérico que o programa deve imprimir no terminal para n = 27.'''
=======
'''Dessa forma, crie um programa que imprima a soma dos n primeiros números da sequência de fibonacci. Escreva o valor numérico que o programa deve imprimir no terminal para n = 27.'''
>>>>>>> d9bb805b2a3bf47831045b94994c84ce3eaddebd

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
result = fibonacci(27)
print(result)
