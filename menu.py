from funciones import *

def ejecutar_menu():
    matriz_notas = inicializar_matriz(5,4,0)
    
    while(True):
        print("Competencia de coina\n1 - Cargar notas\n2 - Mostrar notas\n3 - Ordenar notas por nota promedio\n4 - Peores 3\n5 - Mayores promedio\n6 - Jurado malo\n7 - Sumatoria\n8 - Definir ganador\n9 - Salir\n")
        opcion = pedir_numero_rango("Su opcion: ","Opcion invalida ingrese números entre 1-9\nSu opcion:",1,9)
        if opcion == 1:
            cargar_notas(matriz_notas)
            # hardcodear_datos(matriz_notas)
        elif opcion == 2:
            mostrar_calificaciones(matriz_notas)
        elif opcion == 3:
            criterio = input("Ingrese criterio para ordenar notas por nota promedio, Asendente(ASC) o Descendente(DESC): ")
            ordenar_matriz_por_promedio(matriz_notas,criterio)
            mostrar_calificaciones(matriz_notas)
        elif opcion == 4:
            ordenar_matriz_por_promedio(matriz_notas,"ASC")
            print("\nPEORES 3 PARTICIPANTES EN BASE A SU NOTA PROMEDIO:\n")
            mostrar_peores_tres(matriz_notas)
        elif opcion == 5:
            print("\nPARTICIPANTES QUE SUPERAN EL PROMEDIO TOTAL DE LA COMPETENCIA\n")
            superan_promedio(matriz_notas)
        elif opcion == 6:
            jurado_malo(matriz_notas)
        elif opcion == 7:
            numero = pedir_numero_rango("Ingrese un numero entre 3 y 300: ", "ERROR, número fuera de rango (3-300). Intente de nuevo: ", 3, 300)
            sumar_notas_por_numero(matriz_notas,numero)
        elif opcion == 8:
            determinar_ganador(matriz_notas)
        elif opcion == 9:
            print("Saliendo...")
            break
        limpiar_consola() 
ejecutar_menu()
