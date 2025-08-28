n_notas = int(input("Ingrese la cantidad de notas: "))

aprobadas = 0
desaprobadas = 0
suma_total = 0
suma_aprobadas = 0
suma_desaprobadas = 0
promedio_aprobadas = 0
promedio_desaprobadas = 0

for i in range(n_notas):
    nota = float(input("Ingrese la nota " + str(i + 1) + ": "))
    suma_total = suma_total + nota

    if nota >= 70:
        aprobadas = aprobadas + 1
        suma_aprobadas = suma_aprobadas + nota
    else:
        desaprobadas = desaprobadas + 1
        suma_desaprobadas = suma_desaprobadas + nota

promedio_total = suma_total / n_notas

if aprobadas > 0:
    promedio_aprobadas = suma_aprobadas / aprobadas
else:
    promedio_aprobadas = 0

if desaprobadas > 0:
    promedio_desaprobadas = suma_desaprobadas / desaprobadas
else:
    promedio_desaprobadas = 0


print("Notas aprobadas: ", aprobadas)
print("Notas desaprobadas: ", desaprobadas)
print("Promedio todas las notas: ", promedio_total)
print("Promedio todas las notas aprobadas: ", promedio_aprobadas)
print("Promedio todas las notas: ", promedio_desaprobadas)