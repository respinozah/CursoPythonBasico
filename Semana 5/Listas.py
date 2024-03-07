listaHomogenea = [10,10,20,50,30]

listHeterogenea = [1, "Python", 3, 14, False]

lista1 = [5, 6, 8]
listaconcatenar = [4, 5, 9]

lista1.extend(listaconcatenar) #salida: 5, 6, 8, 4, 5, 9

largo_Lista=len(lista1)
print(largo_Lista) #Salida: 6

lista1.append(60)

lista1.insert(2, 70) #es agregar 70 en la posicion 2

lista1.remove(60) #es por el valor

lista1.pop(1) #remueve el dato en el indice 1

lista1.index(70) #retorna el indica del valor 70

lista1.count(5) #cuenta la cantidad de veces que un elemento esta en una lista

lista1.sort()

lista1.reverse()

lista = ['a', 'e', 'i', 'o', 'u']
for indice, valor in enumerate (lista):
    print(f"")