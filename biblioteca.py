import json

def menu():
    print('''            
            1- Cargar archivo: Se pedirá el nombre del archivo y se cargarán en una lista los elementos del mismo.
            2- Imprimir lista: Se imprimirá por pantalla la tabla (en forma de columnas) con los datos de los servicios.
            3- Asignar incremento: Se deberá hacer uso de una función lambda que asignará a cada servicio un 10% más en el precio unitario.
            4- Filtrar por tipo: Se deberá generar un archivo igual al original, pero donde solo aparezcan servicios del tipo seleccionado por el usuario.           
            5- Mostrar servicios: Se deberá mostrar por pantalla un listado de los servicios ordenados por cliente de manera ascendente.
            6- Guardar
            7- Salir.
          ''')
    opcion = int(input("Opción: "))
    return opcion

def cargar_archivo(nombre:str)->list:
    '''
    carga el contenido de un json
    recibe el nombre del archivo que se cargará
    retorna una lista con los datos cargados
    '''
    try:
        with open(nombre, "r") as archivo:
            resultado = json.load(archivo)

        return resultado
    except FileNotFoundError:
        print("Archivo no encontrado")
        return False

def mostrar_todos_los_datos(lista:list):
    '''
    recibe una lista de diccionarios a mostrar
    '''
    if lista:
        print(f"{'ID Servicio':<15} {'Descripción':<25} {'Tipo':<10} {'Precio Unitario':<15} {'Cantidad':<10} {'Cliente':<20}")
        
    for e_lista in lista:
        print(f"{e_lista['id_servicio']:<15} {e_lista['descripcion']:<25} {e_lista['tipo']:<10} {e_lista['precioUnitario']:<15} {e_lista['cantidad']:<10} {e_lista['cliente']:<20}")

def recordar_pasar_punto1():
    '''
    no recibe nada
    muestra un recordatorio para cargar el archivo
    '''
    print("Primero debe pasar por el punto 1")


def incrementar_10_por_ciento(lista: list, clave: str) -> list:
    '''
    recibe una lista de diccionario en la cualtrabajo y la clave del diccionario con la cual trabajaré (precio unitario)
    retorna una lista de diccionario con la clave (precio unitario) incrementada en un 10%
    '''

    incrementar_precio = lambda num: (num * 1.1) if num > 0 else "error"
    
    for e_lista in lista:
        precio_nuevo = incrementar_precio(float(e_lista[clave]))

        e_lista[clave] = precio_nuevo
    
    return lista

def filtrar_tipo(lista: list, tipo: str) -> list:
    '''
    recibe una lista de diccionario en la cual trabajo y tipo el cual uso para filtrar
    retorna una lista de diccionarios filtrado con el tipo
    '''

    nueva_lista = []
    for e_lista in lista:
        if e_lista["tipo"] == tipo:
            nueva_lista.append(e_lista)
    return nueva_lista 


def ordenar_lista_por_cliente(lista: list, tipo: str) -> list:
    '''
    recibe una lista de diccionario en la cual trabajaré para ordenarla con respecto al parametro 'tipo'
    retorna una lista ya ordenada según el tipo con el cual ordené
    '''

    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if tipo == "ascendente" and (lista[i]["cliente"] > lista[j]["cliente"]):
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
            elif tipo == "descendente" and (lista[i]["cliente"] < lista[j]["cliente"]):
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
    return lista

def recordar_pasar_punto5():
    '''
    no recibe nada
    muestra un recordatorio para pasar por el punto 5 el cual ordena por orden ascendente a los clientes
    '''
    print("Antes debe pasar por el punto 5")

def despedida():
    '''
    no recibe nada
    muestra un mensaje de despedida al seleccionar la opcion "Salir" como verificacion de salida del programa
    no es necesario pasar por el punto 1 o el punto 5
    '''
    print("Saliste del programa")


