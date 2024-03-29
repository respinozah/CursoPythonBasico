import time

nombre = str(input("Digite su nombre: "))
a = int(input("Indique cunates veces desea que su nombre se imprima: "))

for i in range (a):
    print(i, nombre)
    time.sleep(1)
