archivo = open("prueba.txt", "w")
#La "w" crea el archivo y sobreescribe con uno en blanco


archivo = open("prueba.txt", "a")
archivo.write("Hola\n")
archivo.write("Como estas\n")
archivo.close()
#La "a" es de append


archivo = open("prueba.txt", "r")
texto = archivo.read()
print(texto)
archivo.close()
#La "r" es de read, para leer todo el archivo en una variable