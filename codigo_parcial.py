from biblioteca import *
import json

#sirven para no dejar avanzar si no se cumple la condicion de pasar por las opciones que indican
bandera_primera_opcion = False 
bandera_quinta_opcion = False

while True:
    opcion = menu()

    if opcion == 1:
        nombre_archivo = input("Ingrese el nombre del archivo: ")
        lista_nueva = cargar_archivo(nombre_archivo)

        if lista_nueva:
            bandera_primera_opcion = True
            print("Archivo cargado")
        else:
            print("El archivo no se pudo cargar")
    
    elif opcion == 2:
        if bandera_primera_opcion == True:
            mostrar_todos_los_datos(lista_nueva)
        else:
            recordar_pasar_punto1()
    
    elif opcion == 3:
        if bandera_primera_opcion == True:
            precio_actualizado = incrementar_10_por_ciento(lista_nueva, "precioUnitario")
            mostrar_todos_los_datos(precio_actualizado)
        else:
            recordar_pasar_punto1()
    
    elif opcion == 4:
        if bandera_primera_opcion == True:
            tipo = input("Ingrese el tipo para filtrar: ")
            lista_filtrada = filtrar_tipo(lista_nueva,tipo)

            if lista_filtrada:
                with open("servicios_filtrado_por_tipo.json", "w") as archivo:
                    json.dump(lista_filtrada, archivo, indent=4)
                print("Se guardó con éxito")
                mostrar_todos_los_datos(lista_filtrada)
            else:
                print("No se pudo encontrar")

        else:
            recordar_pasar_punto1()
    
    elif opcion == 5:
        if bandera_primera_opcion == True:
            lista_ordenada = ordenar_lista_por_cliente(lista_nueva,"ascendente")
            mostrar_todos_los_datos(lista_ordenada)

            if lista_ordenada:
                bandera_quinta_opcion = True
                print("Archivo cargado")
            else:
                print("No se pudo cargar el archivo")

        else:
            recordar_pasar_punto1()
    
    elif opcion == 6:
        if bandera_primera_opcion == True and bandera_quinta_opcion == True:
            with open("servicios_ordenados.json", "w") as archivo:
                json.dump(lista_ordenada, archivo, indent=4)
            print("Se guardó con éxito")

        else:
            if not bandera_primera_opcion:
                recordar_pasar_punto1()
            elif not bandera_quinta_opcion:
                recordar_pasar_punto5()
    
    elif opcion == 7:
        despedida()
        break


