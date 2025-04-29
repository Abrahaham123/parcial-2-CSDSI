from datetime import datetime
from collections import defaultdict

usos = defaultdict(list)

archivo = open("iteracciones.txt", "r")
for linea in archivo:
    nombre, fecha_str = linea.strip().split(",")
    fecha = datetime.strptime(fecha_str, "%m/%d/%Y")
    usos[nombre].append(fecha)
archivo.close()

print("Promedios de uso (en días) por programa:\n")

for programa, fechas in usos.items():
    fechas.sort()

    if len(fechas) < 2:
        print(programa + ": Solo una sesión registrada")
        continue

    diferencias = []
    for i in range(1, len(fechas)):
        delta = (fechas[i] - fechas[i - 1]).days
        diferencias.append(delta)

    promedio = sum(diferencias) / len(diferencias)
    print(programa + ": Promedio de " + str(round(promedio, 2)) + " días entre sesiones")
