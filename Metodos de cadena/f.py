fecha = input("Introduce la fecha que deseas separar en formato DD/MM/AAAA: ")
print(type(fecha))
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
print(mesaño)
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)