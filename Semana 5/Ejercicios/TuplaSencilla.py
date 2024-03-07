import os
os.system("cls")

agendaDeHoy = ("trabajar", "cocinar", "nadar", "jugar xbox", "dormir", "barrer")
#agendaDeHoy = ("cocinar", "nadar", "jugar xbox", "dormir", "barrer")
#agendaDeHoy = ()

print("\nCuantas actividades hay que hacer hoy?")
if len(agendaDeHoy) > 0:
    print(f"-Hoy hay {len(agendaDeHoy)} actividades")
else:
    print("-Hoy no hay actividades en agenda")

print("\nHay que trabajar hoy?")
if agendaDeHoy.count("trabajar") > 0:
    print(f"-Si, trabajar es tu actividad {agendaDeHoy.index("trabajar") + 1} de hoy.")
else:
    print("-Hoy no hay que trabajar")

print("\nCuales son las actividades de hoy en orden alfabetico?")
agendaDeHoy = sorted(agendaDeHoy)
print(f"-Las actividades de hoy en orden alfabetico son: {agendaDeHoy}")

print(f"\nLa actividad con mas letras es: {max(agendaDeHoy)}")
print(f"\nLa actividad con menos letras es: {min(agendaDeHoy)}")