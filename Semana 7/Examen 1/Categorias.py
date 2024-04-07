#BORRAR
import os

categorias = {}

#BORRAR
def main():
    os.system("cls")
    global categorias
    """
    print(" Categorias:")
    print(categorias)
    print(categorias.keys())
    categoria = "Electronicos"

    if existeCategoria(categoria):
        print(f"La categoria {categoria} existe.")
    else:
        print(f"La categoria {categoria} no existe.")
    
    subCategoria = "SubCategoriaNoValida"
    subCategoria = "Educativo"
    if existeSubCategoria(categorias, subCategoria):
        print(f"Si existe la subcategoria {subCategoria}.")
    else:
        print(f"No existe la subcategoria {subCategoria}.")
    """
    agregarCategoria(categorias)

def agregarCategoria(categorias, strCategoriap):
    
    print("Categoria agregada")


def existeCategoria(categoria):
    if categoria in categorias:
        return True
    else:
        return False

def existeSubCategoria(categorias,strSubCategoriap):
    for subCategorias in categorias.values():
        for strSubCategoria in subCategorias:
            if strSubCategoria == strSubCategoriap:
                return True
    return False

def iniciarCategorias():
    global categorias
    categorias = {
        "Deportes":["Ciclismo", "Futbol", "Natacion"],
        "Electronicos":["Entretenimiento", "Educativo", "Ciencia"],
        "Hogar":["Cocina", "Dormitorio", "Sala"]
    }
    return categorias

if __name__ == "__main__":
    iniciarCategorias()
    main()