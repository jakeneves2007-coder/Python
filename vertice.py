import math

def calcula_vertice(a, b, c):
    x_v = -b / (2 * a) #valor de x do vértice
    y_v = a * x_v ** 2 + b * x_v + c #valor de y do vértice usando a fórmula f(x) = ax² + bx + c

    # Arredonda com math.floor()
    x_v_floor = math.floor(x_v)
    y_v_floor = math.floor(y_v)
    return (x_v_floor, y_v_floor)

a = int(input("Digite o número de a: "))
b = int(input("Digite o número de b: "))
c = int(input("Digite o número de c: "))

result= calcula_vertice(a,b,c)
print(f'Os vértices são:{result}')