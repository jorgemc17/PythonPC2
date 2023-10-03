""" 
Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
}
Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos. 
"""
alumnos = []
cantidad_alumnos = int(input("Ingrese el número de alumnos: "))

for i in range(cantidad_alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la calificación {j + 1} del alumno {nombre}: "))
        notas.append(nota)
    alumno = {"Alumno": nombre, "Notas": notas}
    alumnos.append(alumno)

print("\nListado de Alumnos:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}")
    print(f"Notas: {alumno['Notas']}\n")

