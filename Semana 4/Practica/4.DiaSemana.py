import os
os.system("cls")

diasSemana = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")

diaSeleccionado = int(input("Ingrese un dia entre el 1 y el 7: "))
if diaSeleccionado >= 1 and diaSeleccionado <= 7:
    print(f"-Ha seleccionado el dia de la semana {diasSemana[diaSeleccionado-1]}.")
else:
    print("-Opcion invalida.")