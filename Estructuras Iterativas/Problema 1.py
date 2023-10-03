""" Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
en el rango de 1500 y 2700 (ambos incluidos).
"""
num = 1500
while num <= 2700:
    if num % 35 == 0:
        print('Hola somos los múltiplos de 7 y 5:   ', num)
    elif num %7 == 0:
        print('Hola somos los múltiplos de 7:       ', num)
    elif num %5 == 0 :
        print('hola somos los múltiplos de 5:       ', num)
    num += 1 
