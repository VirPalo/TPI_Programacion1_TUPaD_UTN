paises_de_prueba = [
    {'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400, 'continente': 'America'},
    {'nombre': 'Japón', 'poblacion': 125800000, 'superficie': 377975, 'continente': 'Asia'},
    {'nombre': 'Brasil', 'poblacion': 213993437, 'superficie': 8515767, 'continente': 'America'},
    {'nombre': 'Alemania', 'poblacion': 83149300, 'superficie': 357022, 'continente': 'Europa'}
]

#Ordenamiento de paises 
def ordenamiento(paises):
    valido = ["nombre", "poblacion", "superficie"] #unicas opciones validas a ingresar

    ordenar_por = input("Desea ordenar los paises por:'Nombre', 'Poblacion' o 'Superficie': ").lower()
    if ordenar_por not in valido:
        print("Dato ingresado invalido.")
        return paises, "error"

    #Ordenados alfabeticamente.
    elif ordenar_por == "nombre":
        paises_ordenados = sorted(paises, key=lambda pais: pais['nombre'])
     #Ordenados po poblacion.
    elif ordenar_por == "poblacion":
        paises_ordenados = sorted(paises, key=lambda pais: pais['poblacion'])
    #Ordenados por superficie.
    elif ordenar_por == "superficie":
        asc_o_desc = input("\nDe forma Ascendente o Descendente? \n") 

        if asc_o_desc == "ascendente":
            paises_ordenados= sorted(paises, key=lambda pais: pais['superficie'])

        elif asc_o_desc == "descendente":
            paises_ordenados = sorted(paises, key=lambda pais: pais['superficie'], reverse = True)

        else:  #Si la respuesta es invalida.
            print("Respuesta invalida")
            return paises, "error" #Si se escribe mal ascendente o descendente.
   
    return paises_ordenados, ordenar_por




#Estadisticas
def estadisticas(paises):
        print("\nEstadisticas a mostrar: ")
        print("1. Paises con mayor y menor poblacion.")
        print("2. Promedio de poblacion.")
        print("3. Promedio de superficie.")
        print("4. Cantidad de paises por continente.")

        eleccion= input("Ingrese el numero de la opcion a realizar: ")
        valido = ["1", "2","3","4"]

        if eleccion not in valido:
            print ("Dato ingresado invalido..\n")
            
        elif eleccion == "1": #Pais con mayor y menor poblacion
            mayor_poblacion = max(paises, key=lambda pais: pais['poblacion'])
            menor_poblacion = min(paises, key=lambda pais: pais['poblacion'])
            print(f"\nEl pais con mayor poblacion es:{mayor_poblacion['nombre']}({mayor_poblacion['poblacion']})")
            print(f"El pais con menor poblacion es:{menor_poblacion['nombre']}({menor_poblacion['poblacion']})\n")
        elif eleccion == "2": #Promedio de poblacion
            total = 0
            for pais in paises:
               buscador = pais['poblacion'] #Entra a la poblacion de cada pais
               total += buscador #suma cada dato dentro de poblacion.
            promedio = total / len(paises)
            print("\nEl promedio de poblacion del total de paises es:", promedio, "\n")
        elif eleccion == "3": #Promedio de superficie
            total = 0
            for pais in paises:
                buscador = pais['superficie']
                total += buscador
            promedio = total / len(paises)
            print("\nEl promedio de superficie del total de paises es:", promedio,"\n")
        elif eleccion == "4": #Cantidad de paises por continente
            contador = {} #Diccionario para guardar continente y la cantidad de paises.
            for pais in paises:
                continente = pais['continente']
                if continente in contador: 
                    contador[continente] += 1 
                else:
                    contador[continente] = 1
            for continente, cantidad in contador.items():
                print(f"{continente}: {cantidad} países")
              
#Programa principal (MENU)
 
def menu():
    print("\n MENU ")
    print("1. Buscar paises.")
    print("2.Filtrar paises.")
    print("3. Ordenar paises.")
    print("4. Mostrar estadisticas.")
    print("O. Salir del menu.")

def menu_opciones():
      paises_actualizados = list(paises_de_prueba) 
    
      while True: #Para que el menu se repita hasta que opcion sea 0.
        menu()

        opcion = (input("Ingrese el numero de la opcion de a realizar: "))
        if opcion not in ["0","1", "2", "3", "4"]:
            print ("Debe ingresar un dato valido.")
            continue

        if opcion == "1":
            ...
        elif opcion == "2":
            ...
        elif opcion == "3": 
            paises_ordenados, ordenado_por = ordenamiento(paises_actualizados) #La primera variable contiene la lista ordenada y la segunda el tipo del orden.

            if ordenado_por != "error": #verifica si hay error y continua con el programa.
                paises_actualizados = paises_ordenados
                print(f"\nLista de países ordenada por {ordenado_por}")

                for pais in paises_ordenados:
                    if ordenado_por == "nombre":
                        print(f" - {pais['nombre']}") #Para que el nombre del pais solo se repita una vez.
            
                    else:
                        valor_orden  = pais[ordenado_por] #esto contiene el nombre del pais y el valor del orden.
                        print(f" - {pais['nombre']} su {ordenado_por.capitalize()}: {valor_orden}")
        elif opcion == "4":
            estadisticas(paises_de_prueba)
        elif opcion == "0":
            print("Gracias por usar el menu. Adios!")
            break
        else: 
            print("Dato ingresado invalido.")

menu_opciones()

