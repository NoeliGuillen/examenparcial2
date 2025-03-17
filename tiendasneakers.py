sneakers1 = {
    'nombre': 'Nike Air Force 1',
    'marca': 'Nike', 
    'precio': 2500.0,
    'stock': 10,
    'ID': 1
}
sneakers2 = {
    'nombre': 'Adidas Superstar', 
    'marca':  'Adidas',
    'precio':  2200.0, 
    'stock':   5,
    'ID': 2
}
sneakers3 = {
    'nombre': 'Puma RS-X',
    'marca':  'Puma',
    'precio':  2700.0,
    'stock':   0,
    'ID': 3
}

#inicializar 
sneakers_list = []
sneakers_list.append(sneakers1)
sneakers_list.append(sneakers2)
sneakers_list.append(sneakers3)

#metodo para imprimir lista completa 
def ImprimirListaSneakers(list_sneakers):
    for i, sneaker in enumerate(list_sneakers, start=1): #enumerate sirve para listar
        print(f"{i}. {sneaker['nombre']} ({sneaker['marca']})")
        print(f"   Precio: ${sneaker['precio']}")
        print(f"   Stock: {sneaker['stock']} unidades")
        print(f"   ID: {sneaker['ID']}")
        print("-" * 30)  
#metodo para imprimir un solo sneaker
def imprimirSneaker(sneaker):
    print("-" * 30) 
    print(f"{sneaker['nombre']} ({sneaker['marca']})")
    print(f"   Precio: ${sneaker['precio']}")
    print(f"   Stock: {sneaker['stock']} unidades")
    print(f"   ID: {sneaker['stock']}")
    print("-" * 30) 

#metodo para asignar ID
def asignar_ids():
    for index, sneaker in enumerate(sneakers_list, start=1):
        sneaker['ID'] = index  # ID secuencial

#metodo para agregar    
def AgregarSneaksNuevos ():
    new_id=sneakers_list.__len__() #Contar el número de modelos 
    ingresoNombre = input("Ingresa el nombre del modelo nuevo: ")
    ingresoMarca=input("Ingresa marca: ")
    ingresoPrecio=float(input("Ingresa precio: "))
    ingresoStock=int(input("Ingresa Stock disponible: "))
    nuevo_sneaker= {
         "nombre": ingresoNombre,
         "marca": ingresoMarca,
         "precio": ingresoPrecio,
         "stock": ingresoStock,
         "ID": new_id+1}
    sneakers_list.append(nuevo_sneaker)
    return nuevo_sneaker

#metodo para dar de baja 
def baja_sneaker():
    print("SNEAKERS EN STOCK")
    ImprimirListaSneakers(sneakers_list)
    try:
        baja_id = int(input("Ingresa el ID del modelo a dar de baja: "))
    except ValueError:
        print("Error: Debes ingresar un número.")
        return
    # Buscar el sneaker en la lista
    for sneaker in sneakers_list:
        if sneaker['ID'] == baja_id:
            sneakers_list.remove(sneaker)
            asignar_ids()
            print(f"El sneaker con ID {baja_id} ha sido eliminado.")
            return
    
    print("El ID ingresado no existe en la lista.")

#metodo parea modificar
def modificar_sneaker():
    if not sneakers_list:
        print("No hay sneakers en la lista.")
        return
    ImprimirListaSneakers(sneakers_list)  
    try:
        modificar_id = int(input("Ingresa el ID del modelo a modificar: "))
    except ValueError:
        print("Error: Debes ingresar un número.")
        return
    # Buscar el sneaker por ID
    for sneaker in sneakers_list:
        if sneaker["ID"] == modificar_id:
            while True:
                print("\n¿Qué deseas modificar?")
                print("1. Nombre")
                print("2. Marca")
                print("3. Precio")
                print("4. Stock disponible")
                print("5. Salir y regresar al menú principal")
                opcion = input("Ingresa el número de la opción: ")
                if opcion == "1":
                    nuevo_nombre = input("Ingresa el nombre correcto del modelo: ")
                    sneaker["nombre"] = nuevo_nombre
                    print(f"✅ El nombre se ha modificado a {nuevo_nombre}")
                elif opcion == "2":
                    nueva_marca = input("Ingresa la nueva marca del modelo: ")
                    sneaker["marca"] = nueva_marca
                    print(f"✅ La marca se ha modificado a {nueva_marca}")
                elif opcion == "3":
                    try:
                        nuevo_precio = float(input("Ingresa el nuevo precio para el modelo: "))
                        sneaker["precio"] = nuevo_precio
                        print(f"✅ El precio se ha modificado a ${nuevo_precio}")
                    except ValueError:
                        print("⚠️ Error: Ingresa un valor numérico válido.")
                elif opcion == "4":
                    try:
                        nuevo_stock = int(input("Ingresa el nuevo stock disponible del modelo: "))
                        sneaker["stock"] = nuevo_stock
                        print(f"✅ El stock se ha modificado a {nuevo_stock} unidades")
                    except ValueError:
                        print("⚠️ Error: Ingresa un número entero válido.")

                elif opcion == "5":
                    print("🔙 Regresando al menú principal...")
                    return  

                else:
                    print("⚠️ Opción no válida, intenta de nuevo.")
            break 
    else:
        print("⚠️ El ID ingresado no existe en la lista.")
#Metodos de orden 
def consultar_sneakers():
    print("Bienvenido a la sección de consulta de sneakers disponibles.")
    print("¿Cómo te gustaría visualizar los sneakers disponibles?")
    print("1. Ordenados por precio")
    print("2. Ordenados por marca")
    print("3. Imprimir todo por ID")

    opcion = input("Ingresa el número de la opción: ")
    # Filtrar sneakers con stock disponible
    sneakers_disponibles = [sneaker for sneaker in sneakers_list if sneaker["stock"] > 0]
    if not sneakers_disponibles:
        print("No hay sneakers disponibles en stock.")
        return
    if opcion == "1":
        # Ordenar por precio (menor a mayor)
        sneakers_ordenados = sorted(sneakers_disponibles, key=lambda x: x["precio"])
        print("\nSneakers disponibles ordenados por precio:")
        ImprimirListaSneakers(sneakers_ordenados)
    elif opcion == "2":
        # Ordenar por marca (alfabéticamente)
        sneakers_ordenados = sorted(sneakers_disponibles, key=lambda x: x["marca"].lower())  # Usa lower() para evitar problemas con mayúsculas
        print("\nSneakers disponibles ordenados por marca:")
        ImprimirListaSneakers(sneakers_ordenados)
    elif opcion == "3":
        ImprimirListaSneakers(sneakers_list)
    else:
        print("Opción no válida, por favor selecciona una opción válida.")

#Bienvenida 
print(f"Bienvenido al Gestor de Sneakers!")
while True:
    print("¿Que deseas hacer el día de hoy?")
    print("1. Dar de alta modelos nuevos")
    print("2. Dar de baja de modelos viejos")
    print("3. Modificar los datos de un modelo")
    print("4. Consultar modelos disponibles")
    print("5. Salir")
    opcion = input("\nElige una opción: ") 
    if opcion == "1":
        #Funcion 1: Dar de alta modelos nuevos-----------------------------------------
        sneaker=AgregarSneaksNuevos() 
        print(f"Listo, diste de alta:")
        imprimirSneaker(sneaker)
        #-----------------------------------------------------------------------------
    elif opcion == "2":
        #Funcion 2: Baja de modelos viejos--------------------------------------------- 
        baja_sneaker()
        #------------------------------------------------------------------------------
    elif opcion == "3":
        # Función para modificar los datos de un sneaker--------------------------------
        modificar_sneaker()
        #--------------------------------------------------------------------------------
    elif opcion == "4":
        #Funcion 4: Consulta de los sneakers disponibles, ordenados por precio o marca---
        consultar_sneakers()
        #--------------------------------------------------------------------------------
    elif opcion == "5":
        #Funcion 5: Salir ---------------------------------------------------------------
        print("Saliendo del programa...Ten un buen día")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
