""" 
Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
Ejemplo:
Número ingresado: 15789000 y Dígito: 0
Cantidad de veces 0 en el número: 4
Nota: Para resolver este problema, algunos tipos de datos dentro de python contemplan un método
count. """
def contar(numero_entero,digito):
    contador = str(numero_entero).count(str(digito))
    return contador

numero_entero = int(input("Ingrese un número entero: "))
digito = int(input("Ingrese el dígito: "))
cantidad = contar(numero_entero, digito)
print(f"Cantidad de veces {digito} en el número:  {cantidad}")
