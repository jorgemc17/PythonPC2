""" Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores """

def desarrollo_Fibonacci(limite):
    a, b = 0, 1
    lista=[a]
    while b <= limite:
        lista.append(b)
        a, b = b, a + b 
    return lista
maximo = 50
secuencia=desarrollo_Fibonacci(maximo)
print(f"Esta es la serie: {secuencia}")