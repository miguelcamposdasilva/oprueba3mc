import json, os, time


def seleccionar_opcion(max_value):
    opcion = 0
    while True:
        try:
            opcion = int(input("Ingrese una opción >> "))
        except:
            pass
        if opcion < 1 or opcion > max_value:
            input("Opción inválida, intente nuevamente >> ")
        else:
            return opcion

def start_program():
    while True:
        menu_principal()
        opcion = seleccionar_opcion(5)
        
        if opcion == 1:
            mantenedor_categorias()
        elif opcion == 2:
            return
        input()

if __name__ == "__main__":
    start_program()


def menu_principal():
    print("***************************")
    print("*      MUNDO LIBRO        *")
    print("***************************")
    print("1- Mantenedor de Categorias")
    print("2- Reportes")
    print("3 - Salir")
    opc = int(input("Ingrese una opcion:"))
    if opc == 1:
        mantenedor_categorias()

    

def mantenedor_categorias():
    print("***************************")
    print("*  MANTENEDOR CATEGORIAS  *")
    print("***************************")
    print("1- Agregar Categoria")
    print("2- Editar categoria")
    print("3 - Eliminar Categoria")
    print("4 - Buscar Categoria")
    print("5 - Salir")
    
    opc = int(input("Ingrese una opcion:"))
    if opc == 1:
        agregar_categoria()
    elif opc == 2: 
        editar_categoria()
    elif opc ==3:
        eliminar_categoria()
    elif opc == 4: 
        buscar_categoria()
    elif opc ==5:


def leer_archivo_json(leer):
    try:
        with open(leer, 'r') as archivo:
            return json.load(archivo)
    except:
        return []

biblioteca_json = "biblioteca.json"

def guardar_archivo_json(guardar, data):
    try:
        with open(guardar, 'w') as archivo:
            json.dump(data, archivo, indent=4)
    except:
        return []

def agregar_categoria(categoriaid:int,nombrepar:str):
    os.system("cls")
    print("----Agregar categoria-----:")
    biblioteca = leer_archivo_json (biblioteca_json)
    
    categoria = input("Ingrese la nueva categoria: ")
    nombre = input("Ingrese el nombre de la categoria: ")

    nueva_categoria = {
        "CategoriaID": categoria,
        "Nombre": nombre
    }
    
    biblioteca.append(nueva_categoria)
    
    guardar_archivo_json(biblioteca_json, biblioteca)

def editar_categoria():
    os.system("cls")
    print("------Editar Categorias-----")
    biblioteca = leer_archivo_json(biblioteca_json)
    

    id_categoria = input("Ingrese el ID de la categoria que desea editar: ")
    nueva_categoria = input("Ingrese el nuevo nombre de la categoria: ")

    for categoria in biblioteca:
        if categoria ['CategoriaID'] == id_categoria:
            categoria ['Nombre'] = nueva_categoria
            break
    
    guardar_archivo_json(biblioteca_json, biblioteca)


def eliminar_categoria():
    os.system("cls")
    print("----Eliminar Categoria----")
    biblioteca = leer_archivo_json(biblioteca_json)
    
    id_categoria = input("Ingrese el ID de la categoria que desea eliminar>> ")
    categorias_restantes= []
    
    for categoria in biblioteca:
        if categoria ['CategoriaID'] != id_categoria:
            categorias_restantes.append(categoria)
    
    guardar_archivo_json(biblioteca_json, categorias_restantes)


def buscar_categoria():
    with open("biblioteca.json", mode = "r") as lecturajson:
        leerjson = json.load(lecturajson)

        print(" ID    CATEGORIA ")
        for i in leerjson["Categoria"]:
            print( i["CategoriaID"], i["Nombre"])





