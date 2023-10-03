""" 
Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento. """
def calcular_factorial(numero_a_procesar):
    factorial=1
    lista_factorial=[]
    for i in range(numero_a_procesar):
        factorial=factorial*(i+1)
        lista_factorial.append(i+1)
    print(f"El resultado del factorial de {numero_a_procesar} es: {factorial}")
    print(f"Los numeros del factorial son: {lista_factorial}")

numero_a_procesar = int(input("Digite el factorial de : "))
calcular_factorial(numero_a_procesar)

