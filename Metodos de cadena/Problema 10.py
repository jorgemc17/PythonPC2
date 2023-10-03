""" 
En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las
fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en
lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente
en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son
ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de
1636!
Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
la lista abajo:
[
"Enero",
"Febrero",
"Marzo",
"Abril",
"Mayo",
"Junio",
"Julio",
"Agosto",
"Septiembre",
"Octubre",
"Noviembre",
"Diciembre"
]
Luego, genere esa misma fecha en formato AAAA-MM-DD.
Ejemplos:
- Input: 9/8/1636 | Output: 1636-09-08
- Input: Septiembre 8, 1636 | Output: 1636-09-08
- Input: 1/1/1970 | Output: 1970-01-01 """

diccionario_meses = {
    "Enero": "01",
    "Febrero": "02",
    "Marzo": "03",
    "Abril": "04",
    "Mayo": "05",
    "Junio": "06",
    "Julio": "07",
    "Agosto": "08",
    "Septiembre": "09",
    "Octubre": "10",
    "Noviembre": "11",
    "Diciembre": "12"
}

def transformador_fecha(fecha_digitada):
    palabras = fecha_digitada.split()
    if "/" in fecha_digitada:
        mes, dia, año = fecha_digitada.split("/")
    else:
        mes = diccionario_meses[palabras[0]]
        dia = palabras[1].strip(',')
        año = palabras[2]
    print(f"Fecha formateada: {año}-{mes:02}-{dia:02}")

fecha_digitada = input("Ingrese una fecha (mes/día/año o Mes día, año): ")
transformador_fecha(fecha_digitada)
