""" Escriba una función de Python que tome un número como parámetro y verifique que el número sea
primo o no """
def verificar_primo(numero_entero):
    es_primo = True
    respuesta:str
    for i in range(2, numero_entero):
        if numero_entero % i == 0:
            es_primo = False
            break
    if es_primo:
        respuesta=(f"El número {numero_entero} es primo")
    else:
        respuesta=(f"El número {numero_entero} no es primo, se encontro un divisor: {i}")
    return(respuesta)

numero_entero=int(input("Digite un numero a verificar: "))
print(verificar_primo(numero_entero))

