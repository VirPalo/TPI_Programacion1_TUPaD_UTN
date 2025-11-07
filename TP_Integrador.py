'''
paises_de_prueba = [
    {'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400, 'continente': 'America'},
    {'nombre': 'Japón', 'poblacion': 125800000, 'superficie': 377975, 'continente': 'Asia'},
    {'nombre': 'Brasil', 'poblacion': 213993437, 'superficie': 8515767, 'continente': 'America'},
    {'nombre': 'Alemania', 'poblacion': 83149300, 'superficie': 357022, 'continente': 'Europa'}
]
'''

# Funcion de carga del archivo paises.csv
def carga_archivo():
    paises = []
    with open('paises.csv', 'r', encoding='latin-1') as archivo:
        lineas = archivo.readlines()
        for i in range(1, len(lineas)): # Salto el encabezado del .csv
            datos = lineas[i].strip().split(',')
            pais = {'nombre': datos[0], 'poblacion': int(datos[1]), 'superficie': int(datos[2]), 'continente': datos[3]}
            paises.append(pais)
            
        return paises

# OPCIÓN 1: Función para agregar un país ----------


#---Funcion para solo numero positivo
def num_positivo(mensaje):
    while True: 
        try: #permite solo ingresar numeros
            poblacion_pais = int(input(mensaje))
            if poblacion_pais <= 0: #solo permite ingresar nuemeros mayores a 0.
                print("Debe ingresar un numero mayor a 0")
                continue #vuelve al inici del while.
            return poblacion_pais #si es valido
        except ValueError:
            print("Dato ingresado invalido.")

#---Funcion solo para continentes validos---
def continente_valido(nombre_pais):
    continentes_validos = ["america", "europa", "asia", "africa", "oceania", "antartida"]

    while True:
        print(f"A qué continente pertenece {nombre_pais.capitalize()}?")
        print("\nAsia")
        print("Africa")
        print("America")
        print("Europa")
        print("Oceania")
        print("Antartida")
        continente_pais = input("\nContinente: ").lower()

        if continente_pais not in continentes_validos:
            print("\nDebe ingresar un continente válido. Intente de nuevo.")
            continue
        return continente_pais

def agregar():
    while True:
        nombre_pais = input("\nIngrese el nombre del pais a agregar: ").strip().lower()
        # Si el usuario no ingresa nada
        if nombre_pais == "":
            print("Debe ingresar un nombre. Intente nuevamente.")
            continue
    
        valido = True
        for letras in nombre_pais:
            if not (letras.isalpha() or letras == " "):
                valido = False
                break
        
        if not valido:
            print("Dato ingresado invalido")
            continue

        for pais in paises: #verifica que el pais a agregar no se encuentre ya en la lista.
            if pais['nombre'] == nombre_pais:
                print (f"\nEl pais {nombre_pais.capitalize()} ya se encuentra en la lista de paises.")
                return 
        #si el pais no se encuentra pide los demas datos
        break #su cumple las validaciones sale del bucle 

    poblacion_pais = num_positivo("Ingrese la población del país agregado: ")
    superficie_pais = num_positivo("Ingrese la superficie del país agregado: ")
    continente_pais = continente_valido(nombre_pais)


    pais_nuevo = {
    'nombre' : nombre_pais,
    'poblacion' : poblacion_pais,
    'superficie' : superficie_pais,
    'continente' : continente_pais
     }
    paises.append(pais_nuevo) 
    print("\nPais agregado con exito!")
    print(f"Pais: {nombre_pais.capitalize()}, Poblacion: {poblacion_pais}, Superficie: {superficie_pais}, Continente: {continente_pais.capitalize()}")


    



# OPCIÓN 2: Función para modificar población y superficie de un país ----------


# OPCIÓN 3: Función para buscar paises ----------
def busqueda():
    pais_buscado = input('Ingrese el nombre del país que está buscando: ').strip()
    
    # Coincidencia exacta
    for pais in paises:
        if pais_buscado.lower() == pais['nombre'].lower():
            mostrar_un_pais(pais)
            return
            
    # Coincidencia parcial
    coincidencias_parciales = []
    for pais in paises:
        if pais_buscado.lower() in pais['nombre'].lower():
            coincidencias_parciales.append(pais)
     
    if not coincidencias_parciales: # Verifico que la lista de coincidencias no sea vacia.
        print(f'El país {pais_buscado} no se encuentra en la lista.')
        return
            
    print('\nPaíses con coincidencias parciales: ')
    for pais in coincidencias_parciales:
        print(f'- {pais['nombre']}')
        
    respuesta = input('\n¿Quisiste decir alguno de estos? S/N\n').strip().upper()
    if respuesta == 'S':
        nombre_correcto = input('\nIngrese correctamente el nombre del país: ').strip()
        
        encontrado = False
        for pais in paises: # Vuelvo a buscar la coincidencia exacta con el nombre correcto
            if nombre_correcto.lower() == pais['nombre'].lower():
                mostrar_un_pais(pais)
                encontrado = True
                return
        
        if not encontrado: # Verifico si el nombre correcto ingresado no esta en la lista
            print(f'\nEl país {pais_buscado} no se encuentra en la lista.')
            return
    
    elif respuesta == 'N':
        print(f'\nEl país {pais_buscado} no se encuentra en la lista.')
        
    else:
        print('\nRespuesta inválida.')
        
# Función para mostrar la información de un país
def mostrar_un_pais(pais):
    print('\n--- Información del país ---')
    print(f'Nombre: {pais['nombre']}')
    print(f'Población: {pais['poblacion']:,} habitantes')
    print(f'Superficie: {pais['superficie']:,} km²')
    print(f'Continente: {pais['continente']}')

# OPCIÓN 4: Función para filtrar paises por Continente, por Rango de superficie, por Rango de poblacion ----------
def menu_filtrar_paises():
    
    while True:
        print('\n--- Menu para filtrar ---')
        print('\n1. Filtrar por Continente')
        print('2. Filtrar por Rango de Superficie')
        print('3. Filtrar por Rango de Población')
        print('0. Salir')
        
        opc = input('\nIngrese la opción de filtrado: ')
    
        # Opción para salir del menú de filtrado
        if opc == '0':
            print('Regresa al menú principal.')
            break
             
        # Filtrar por continente
        elif opc == '1':
            filtrar_continente()
            
        # Filtrar por Rango de Superficie
        elif opc == '2':
            filtrar_superficie()
     
        # Filtrar por Rango de Poblacion
        elif opc == '3':
            filtrar_poblacion()
        
        # Opción incorrecta
        else:
            print('\nOpción inválida. Intente de nuevo.')

# Función para mostrar todos los países de una lista 
def mostrar_paises(paises):
    print('\n--- Información de los países: ---\n')
    for pais in paises:
        print(f'Nombre: {pais['nombre']} |Población: {pais['poblacion']:,} habitantes |Superficie: {pais['superficie']:,} km² |Continente: {pais['continente']}')

# Función para mostrar todos los continentes de la lista original
def mostrar_continentes():
    continentes = []
    for pais in paises:
        if pais['continente'] not in continentes:
            continentes.append(pais['continente'])

    print('\nLos continentes en la lista son: ')
    for i in range(len(continentes)):
        print(f'- {continentes[i]}')

# Función para filtrar por continente
def filtrar_continente():
    mostrar_continentes() # Llamada a la función p/mostrar los continentes
    continente = input('\nIngrese el continente para filtrar: ').strip()
    
    paises_filtrados = []
    for pais in paises:
        if continente.lower() == pais['continente'].lower():
            paises_filtrados.append(pais)
    
    if paises_filtrados:
        mostrar_paises(paises_filtrados)
    else:
        print(f'En la lista no existen países del continente {continente}.')

# Función para filtrar por superficie
def filtrar_superficie():
    print('\nPara filtrar por rango de superficie, ingrese la superficie mínima y máxima en km².')
    
    # Valido los valores a ingresar
    while True:
        sup_min = int(input('\nIngrese la superficie mínima del rango: '))
        sup_max = int(input('\nIngrese la superficie máxima del rango: '))
        
        if sup_min < 0 or sup_max < 0:
            print('Valores inválidos. Intente nuevamente ingresando números positivos.')
        
        elif sup_min > sup_max:
            print('La superficie mínima no puede ser mayor que la superficie máxima. Intente nuevamente.')
        
        else:
            break
    
    # Filtrar
    paises_filtrados = []
    for pais in paises:
        if pais['superficie'] >= sup_min and pais['superficie'] <= sup_max:
            paises_filtrados.append(pais)
    
    if paises_filtrados:
        mostrar_paises(paises_filtrados)
    else:
        print('No existen países de la lista en ese rango.')

# Función para filtrar por población
def filtrar_poblacion():
    print('\nPara filtrar por rango de poblacion, ingrese la cantidad mínima y máxima de habitantes.')
    
    # Valido los valores a ingresar
    while True:
        p_min = int(input('\nIngrese la cantidad mínima de habitantes del rango: '))
        p_max = int(input('\nIngrese la cantidad máxima de habitantes del rango: '))
        
        if p_min < 0 or p_max < 0:
            print('Valores inválidos. Intente nuevamente ingresando números positivos.')
        
        elif p_min > p_max:
            print('La población mínima no puede ser mayor que la población máxima. Intente nuevamente.')
        
        else:
            break
    
    # Filtrar
    paises_filtrados = []
    for pais in paises:
        if pais['poblacion'] >= p_min and pais['poblacion'] <= p_max:
            paises_filtrados.append(pais)
    
    if paises_filtrados:
        mostrar_paises(paises_filtrados)
    else:
        print('No existen países de la lista en ese rango.')
     

# OPCIÓN 5: Ordenamiento de paises ----------

def ordenamiento():
    
    while True:
            print("\n-- Menu para ordenar--")
            print("\n1. Ordenar por Nombre")
            print("2. Ordenar por Poblacion")
            print("3. Ordenar por Superfice")
            print("0. Salir")

            ordenar_por = input("Ingrese opcion de ordenamiento: ")
        
            if ordenar_por == "0":
                print("Regresa al menu principal")
                break
            tipo_orden = ""

            #Ordenados alfabeticamente.
            if ordenar_por == "1":
                eleccion = "nombre" #clave para acceder al diccionario.
                paises_ordenados = sorted(paises, key=lambda pais: pais['nombre'])
                #Ordenados po poblacion.
            elif ordenar_por == "2":
                eleccion = "poblacion" #clave para acceder al diccionario.
                paises_ordenados = sorted(paises, key=lambda pais: pais['poblacion'])
            #Ordenados por superficie.
            elif ordenar_por == "3":
                eleccion = "superficie" #clave para acceder al diccionario.
                asc_o_desc = input("\nDe forma Ascendente o Descendente? \n") 

                if asc_o_desc == "ascendente":
                    tipo_orden = "de manera ascendente"
                    paises_ordenados= sorted(paises, key=lambda pais: pais['superficie'])

                elif asc_o_desc == "descendente":
                    tipo_orden = "de manera descendente"
                    paises_ordenados = sorted(paises, key=lambda pais: pais['superficie'], reverse = True)

                else:  #Si la respuesta es invalida.
                    print("Respuesta invalida") #Si se escribe mal ascendente o descendente.
            else:
                print("Dato ingresado invalido.")
                continue #vuelve al inicio del while
            #impresion
            print(f"\nLista de paises ordenada por {eleccion.capitalize()} {tipo_orden}:")
            for pais in paises_ordenados:
                if ordenar_por == "1":
                    print(f" - {pais['nombre']}")
                elif ordenar_por == "2":
                    valor_orden = pais[eleccion]
                    print(f" - {pais['nombre']}, {eleccion.capitalize()}: {valor_orden} habitantes.")
                elif ordenar_por == "3":
                    valor_orden = pais[eleccion]
                    print(f" - {pais['nombre']}, {eleccion.capitalize()}: {valor_orden} km².")


# OPCIÓN 6: Estadisticas ----------
#Funcion para calcular la media
def media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def estadisticas(paises): # Menu de estadisticas.
    while True:
        print("\nQue estadisticas desea ver? ")
        print("1. Paises con mayor y menor poblacion.")
        print("2. Promedio de poblacion.")
        print("3. Promedio de superficie.")
        print("4. Cantidad de paises por continente.")
        print("0. Salir")
        
        eleccion= input("\nIngrese el numero de la opcion a realizar: ")
        
        if eleccion == "0":
            print("Regresa al menu principal.")
            break
            
        elif eleccion == "1": #Pais con mayor y menor poblacion
            mayor_poblacion = max(paises, key=lambda pais: pais['poblacion'])
            menor_poblacion = min(paises, key=lambda pais: pais['poblacion'])
            print(f"\nEl pais con mayor poblacion es: {mayor_poblacion['nombre']} con una poblacion de ({mayor_poblacion['poblacion']})")
            print(f"El pais con menor poblacion es: {menor_poblacion['nombre']} con una poblacion de ({menor_poblacion['poblacion']})\n")
        
        elif eleccion == "2": #Promedio de poblacion
            poblaciones = [pais['poblacion'] for pais in paises]
            promedio = media(poblaciones)
            print("\nEl promedio de población del total de países es:", (promedio), "\n")
        
        elif eleccion == "3": #Promedio de superficie
            superficies = [pais['superficie'] for pais in paises]
            promedio = media(superficies)
            print("\nEl promedio de superficie del total de países es:", (promedio), "\n")
        
        elif eleccion == "4": #Cantidad de paises por continente
            contador = {} #Diccionario para guardar continente y la cantidad de paises.
            print("\nPaises por continente: \n")
            for pais in paises:
                continente = pais['continente']
                if continente in contador: 
                    contador[continente] += 1 
                else:
                    contador[continente] = 1
            for continente, cantidad in contador.items():
                print(f"{continente}: {cantidad} paises")
        else: 
            print("Dato ingresado invalido")
            continue
# Programa principal (MENU) -------------------------------

# Primero se guarda el archivo en una lista de diccionarios.
paises = carga_archivo()

def menu():
    print("\n MENU PRINCIPAL ")
    print("\n1. Agregar un país.")
    print("2. Actualizar población y superficie de un país.")
    print("3. Buscar paises.")  
    print("4. Filtrar paises.")
    print("5. Ordenar paises.")
    print("6. Mostrar estadisticas.")
    print("O. Salir del menu.")

def menu_opciones():
      
      while True: #Para que el menu se repita hasta que opcion sea 0.
        menu()

        opcion = (input("Ingrese el numero de la opcion de a realizar: "))
        if opcion not in ["0","1", "2", "3", "4","5","6"]:
            print ("Debe ingresar un dato valido.")
            continue
        
        if opcion == "1":
            agregar()     

        elif opcion == "2":
            pass
        
    elif opcion == "3":
        busqueda()

    elif opcion == "4":
        menu_filtrar_paises()
        
        elif opcion == "5": 
            ordenamiento()
                        
        elif opcion == "6":
            estadisticas(paises)
            
        elif opcion == "0":
            print("Gracias por usar el menu. Adios!")
            break
        
        else: 
            print("Dato ingresado inválido.")



menu_opciones()