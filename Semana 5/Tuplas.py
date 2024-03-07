tupla = (1,2,3,4,5,6,7,8,9)
print(len(tupla)) # salida: 9

tupla = (1,2,2,2,3,2,4,2,5,2,2,9)
print(tupla.count(2)) # salida: 7
#print(tupla.index(2)) #salida: 1

tupla = ("a", "e", "e", "i", "o", "u")
print(tupla.index("o"))# salida: 4

tupla = (3,9,8,7,5,6,4,5,8)
ordene_tupla = sorted(tupla)
print(ordene_tupla) # salida: [3, 4, 5, 5, 6, 7, 8, 8, 9]

tupla = (10,8,9,7)
print(max(tupla)) # salida: 10
#min

tupla = (False, False, False, True)
print(any(tupla)) # salida: True
print(all(tupla)) # salida: False

#

tupla1 = (1,9,6)
tuplavocales = ('a', 'e', 'e', 'i', 'o', 'u')
tuplaConsolidada = tupla1 + tuplavocales
print(tuplaConsolidada) # salida: (1, 9, 6, 'a', 'e', 'e', 'i', 'o', 'u')

lista = [1,2,3]
print(lista) # salida: [1, 2, 3]
tuplaLista = tuple(lista)
print(tuplaLista) # salida: (1, 2, 3)

tuplaInicial = (1,2,3)
nuevaTupla = (*tuplaInicial,4,5,6,7,8)
print(nuevaTupla) # salida: (1, 2, 3, 4, 5, 6, 7, 8)

tuplaInicial = (1,2,3)
tuplaInicial = (*tuplaInicial,4,5,6,7,8)
print(tuplaInicial) # salida: (1, 2, 3, 4, 5, 6, 7, 8)

#Slicing
#inicio:fin
#rango
#NO ES CON INDICE
tupla = (1,2,3,4,5,6)
tupla = (0,1,2,3,4,5,6)
tuplaNueva = tupla[:3] + (50,60) + tupla[3:]
print(tuplaNueva) # salida