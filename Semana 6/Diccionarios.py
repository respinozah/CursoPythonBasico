diccionario = {"Nombre":"Vanessa", "Edad":30, "Provincia":"San Jose" ,"Pais":"Costa Rica"}
print(diccionario)

tiposClientes = {
    "clienteFrecuente": {"nombre":"Juan", "edad":35},
    "clienteNormal": {"nombre":"Pedro", "edad":27}
}

print(diccionario.get("Edad"))
print(diccionario["Nombre"])

diccionario["Edad"] = 35
print(diccionario.get("Edad"))

del diccionario["Provincia"]
print(diccionario)

#len()
print(len(diccionario))

#keys
print(diccionario.keys())

#Valores de los keys
print(diccionario.values())

#elimina y devuelve un valor asociado a una clave especifica
valor = diccionario.pop("Pais")
print(f"El valor es {valor}.")
print(diccionario)

diccionario = {"Nombre":"Vanessa", "Edad":30, "Provincia":"San Jose" ,"Pais":"Costa Rica"}

#items
print(diccionario.items())

#diccionarios por comprension
palabras = ["Raul", "Jean Ca", "Walter", "Samantha"]
diccionarioDePalabras = {palabra: len (palabra) for palabra in palabras}
print(diccionarioDePalabras)

#elementos combinados
elementosCombinados = ["Vane", 3.14, 50, True, "Vanessa"]
diccionarioCombinado = {str(elemento):type(elemento) for elemento in elementosCombinados}

# par de elementos clave:valor
diccionario ["Canton"]=None
print(diccionario)

diccionario.get("Nombre")

#update
diccionario["Canton"] = "Central"
print("Ojo aqui")
diccionarioInicial = {"numero1":1,"numero2":2}
diccionarioInicial.update({"numero3":3,"numero4":4,"numero2":2.5})
print(diccionarioInicial)

#clear
diccionarioInicial.clear()
print(diccionarioInicial)

#copy
copiaDiccionarioInicial = diccionarioInicial.copy()

#From Keys
diccionarioInicial = {"numero1":1,"numero2":2}
diccionarioInicial.update({"numero3":3,"numero4":4,"numero2":2.5})

#nuevoDiccionario = diccionarioInicial.fromkeys()
diccionarioOriginal = {"Product X":10000, "Product Y":4000, "Product Z":30}
print(diccionarioOriginal)
diccionarioNuevo = diccionarioOriginal.fromkeys(["Product X", "Product Y", "Product Z"], 90000)
print(diccionarioNuevo)

