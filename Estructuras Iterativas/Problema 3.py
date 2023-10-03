""" Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares. """
indice=0
cantidad_pares=0
lista1=[]
respuesta=input("Desea agregar un numero? :")
respuesta=respuesta.upper()
if respuesta == "SI":
    while respuesta == "SI":
        lista1.append(int(input("Ingrese el numero: ")))
        if lista1[indice] % 2 ==0:
            cantidad_pares+=1
        respuesta=input("Desea agregar un numero? :")
        respuesta=respuesta.upper()
        indice+=1
    print(f"Numeros ingresados: {lista1}")
    print(f"Cantidad de numero pares: {cantidad_pares}")
    print(f"Cantidad de numero impares: {len(lista1)-cantidad_pares}")
else:
    print(" Hasta luego entonces.")