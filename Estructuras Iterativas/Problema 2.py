""" Escriba un programa en Python para construir el siguiente patrón.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
* """
altura=9
for i in range(altura):
    if i<5:
        print('*' * (i+1))
    else:
        print('*' * (9-i))
