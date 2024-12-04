import os
import random

# Una competencia de cocina califica a los mejores cocineros de la ciudad.
# Se requieren los siguientes datos:
# -Número de participante (Autoincremental) -> No se pide por input, se genera
# automáticamente y se guarda en la matriz, arranca del 1 en adelante.
# -Voto jurado 1 (1 al 100)
# -Voto jurado 2 (1 al 100)
# -Voto jurado 3 (1 al 100)
# De los 5 participantes que se postularon se requiere lo siguiente:

I_NUMERO = 0
I_JURADO_1 = 1
I_JURADO_2 = 2
I_JURADO_3 = 3

DESC = True
ASC = False

indice = 0

def hardcodear_datos(matriz_votos:list) -> None:
    for fil in range(len(matriz_votos)):
        matriz_votos[fil][I_NUMERO] = random.randint(100,999)
        matriz_votos[fil][I_JURADO_1] = random.randint(0,1000)
        matriz_votos[fil][I_JURADO_2] = random.randint(0,1000)
        matriz_votos[fil][I_JURADO_3] = random.randint(0,1000)
    print("\nDatos hardcodeados con exito\n")

def inicializar_matriz(cantidad_filas : int, cantidad_columnas : int, valor_inicial : any = None) -> list:    
    matriz = []
    
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def limpiar_consola():
    input("Ingrese cualquier boton para continuar...")
    os.system('cls')

def pedir_numero_rango(mensaje:str,mensaje_error:str, minimo:int, maximo:int)->int:
    numero = int(input(mensaje))
    while numero > maximo or numero < minimo:
        numero = int(input(mensaje_error))
    return numero

def pedir_numero_minimo(mensaje:str,mensaje_error:str,minimo:int) -> int:
    numero = int(input(mensaje))
    while numero < minimo:
        numero = int(input(mensaje_error))
    return numero

def calcular_valor_minimo(I_NUMERO:list) -> int:
    minimo = None
    bandera = False
    for i in range(len(I_NUMERO)):
        if bandera == False or I_NUMERO[i] < minimo:
            minimo = I_NUMERO[i]
            bandera = True
    return minimo

def agregar_participante(matriz_notas):
    global indice 
    indice +=1
    print(f"Participante numero {indice}")
    return indice

# 1. Cargar Notas: Se realiza una carga secuencial de todos las notas de cada uno de los
# jurados (Debe ser una matriz)
# NOTA: Las notas son del 1 al 100
def cargar_notas(matriz_notas):
    for fil in range(len(matriz_notas)):
        print("\nCARGO VOTO\n")
        matriz_notas[fil][I_NUMERO] = agregar_participante(matriz_notas)
        matriz_notas[fil][I_JURADO_1] = pedir_numero_rango("Ingrese nota del Jurado 1: ", "ERROR, Ingrese nota valida (Entre 1 y 100)",1,100)
        matriz_notas[fil][I_JURADO_2] = pedir_numero_rango("Ingrese nota del Jurado 2: ", "ERROR, Ingrese nota valida (Entre 1 y 100)",1,100)
        matriz_notas[fil][I_JURADO_3] = pedir_numero_rango("Ingrese nota del Jurado 3: ", "ERROR, Ingrese nota valida (Entre 1 y 100)",1,100)
    print("\nVotos cargados con exito\n")

# 2. Mostrar Votos: Muestra en un lindo formato los siguientes datos:
# Participante, Nota jurado 1, Nota Jurado 2, Nota jurado 3, Nota promedio
def sumar_votos(matriz_votos:list,fila:int) -> int:
    suma_votos = (matriz_votos[fila][I_JURADO_1] + matriz_votos[fila][I_JURADO_2] + matriz_votos[fila][I_JURADO_3])
    return suma_votos
def calcular_promedio(matriz_votos,fila):
    votos_totales = sumar_votos(matriz_votos,fila)
    promedio = votos_totales / len(matriz_votos)
    return promedio

# Funcion final reflejada en el menu
def mostrar_calificaciones(matriz_votos):
    for fil in range(len(matriz_votos)):
        promedio_votos = calcular_promedio(matriz_votos,fil)
        mostrar_votos(matriz_votos[fil])
        print(f"NOTA PROMEDIO: {promedio_votos:.2f}\n")

def mostrar_votos(matriz_votos):
    print(f"PARTICIPANTE NRO: {matriz_votos[I_NUMERO]}")
    print(f"VOTO JURADO 1: {matriz_votos[I_JURADO_1]}")
    print(f"VOTO JURADO 2: {matriz_votos[I_JURADO_2]}")
    print(f"VOTO JURADO 3: {matriz_votos[I_JURADO_3]}")

# 3. Ordenar votos por nota promedio: Se le pide al usuario que ingrese un orden (asc o
# desc) y ordena la matriz por nota promedio.
def ordenar_matriz_por_promedio(matriz:list,criterio:str)->bool:

    for i in range(len(matriz) - 1):
        for j in range(i + 1, len(matriz)):
            promedio_i = calcular_promedio(matriz,i)
            promedio_j = calcular_promedio(matriz,j)

            if (criterio == "ASC" and promedio_i > promedio_j) or (criterio == "DESC" and promedio_i < promedio_j):
                aux = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = aux
    return True

# 4. Peores 3: Mostrar los peores 3 participantes en base a su nota promedio
def peores_tres_promedios(matriz_votos,criterio):
    return ordenar_matriz_por_promedio(matriz_votos,"ASC")
def mostrar_peores_tres(matriz_votos): 
    for fil in range(3):
        promedio_votos = calcular_promedio(matriz_votos,fil)
        mostrar_votos(matriz_votos[fil])
        print(f"NOTA PROMEDIO: {promedio_votos:.2f}\n")
    return matriz_votos

# 5. Mayores promedio: Del promedio total de notas, mostrar a los participantes que
# superan esa nota (siempre tomando la nota promedio)
def calcular_promedio_total(matriz_votos):
    suma_total = 0
    for i in range(len(matriz_votos)):
        suma_total += calcular_promedio(matriz_votos, i)
    if len(matriz_votos) > 0:
        promedio_total = suma_total / len(matriz_votos)
    return promedio_total

def superan_promedio(matriz_votos):
    bandera = False
    promedio_total = calcular_promedio_total(matriz_votos)
    print(f"\nPROMEDIO TOTAL DE NOTAS: {promedio_total:.2f}\n")
    
    for fil in range(len(matriz_votos)):
        promedio_participante = calcular_promedio(matriz_votos,fil)
        if promedio_participante > promedio_total:
            bandera = True
            print(f"PARTICIPANTE NRO: {matriz_votos[fil][I_NUMERO]}")
            print(f"VOTO JURADO 1: {matriz_votos[fil][I_JURADO_1]}")
            print(f"VOTO JURADO 2: {matriz_votos[fil][I_JURADO_2]}")
            print(f"VOTO JURADO 3: {matriz_votos[fil][I_JURADO_3]}")
            print(f"NOTA PROMEDIO: {promedio_participante:.2f}\n")
    if not bandera:
        print("NINGUNO DE LOS PARTICIPANTES SUPERAN LA NOTA PROMEDIO")

# 6. Jurado malo: Mostrar cuál fue el jurado/jurados que puso en promedio las peores
def jurado_malo(matriz_votos):
    
    suma_jurado_1, suma_jurado_2, suma_jurado_3 = suma_jurados(matriz_votos)

    promedio_jurado_1 = suma_jurado_1 / len(matriz_votos)
    promedio_jurado_2 = suma_jurado_2 / len(matriz_votos)
    promedio_jurado_3 = suma_jurado_3 / len(matriz_votos)

    I_NUMERO_jurados = [promedio_jurado_1, promedio_jurado_2, promedio_jurado_3]

    peor_nota = calcular_valor_minimo(I_NUMERO_jurados)

    if peor_nota == promedio_jurado_1:
        jurado_malo = 1
    elif peor_nota == promedio_jurado_2:
        jurado_malo = 2
    else:
        jurado_malo = 3

    print("\nJURADO CON PEOR NOTA PROMEDIO:")
    print(f"Jurado numero {jurado_malo} con promedio de {peor_nota:.2f}")

    return jurado_malo, peor_nota

def suma_jurados(matriz_votos):
    suma_jurado_1 = 0
    suma_jurado_2 = 0
    suma_jurado_3 = 0

    for fil in range(len(matriz_votos)):
        suma_jurado_1 += matriz_votos[fil][I_JURADO_1]
        suma_jurado_2 += matriz_votos[fil][I_JURADO_2]
        suma_jurado_3 += matriz_votos[fil][I_JURADO_3]

    return suma_jurado_1, suma_jurado_2, suma_jurado_3

# 7. Sumatoria: Pedir un número por input (entre 3 y 300) , mostrar los participantes en los
# que la suma de sus tres notas de ese número. En caso de que no haya ninguno
# mostrar un mensaje de error

def sumar_notas_por_numero(matriz_votos,numero):
    
    if not condicion_numeros_rango(numero,3,300):
        return None
    
    bandera = False
    
    print(f"Participantes cuya suma de notas es igual a {numero}:")
    
    for fila in matriz_votos:
        suma_notas = fila[I_JURADO_1] + fila[I_JURADO_2] + fila[I_JURADO_3]
        if suma_notas == numero:
            bandera = True
            mostrar_votos(fila)
    if not bandera:
        print("No se encontraron participantes que la sumatoria de sus notas de el numero ingresado.")

def condicion_numeros_rango(numero,entero_1:int,entero_2:int):
    if numero < entero_1 or numero > entero_2:
        print(f"Error, ingrese números entre {entero_1} y {entero_2}")
        return False
    return True

# 8. Definir ganador: Muestra al ganador de la competencia en base a su nota promedio,
# en caso de haber más de uno, se realiza un desempate entre todos los ganadores.
# En qué consiste el desempate: Cada uno de los jurados debe elegir el número del
# participante que desea que gane, el participante más elegido gana, en caso de no
# haber acuerdo (por ejemplo hay 3 participantes que ganaron y cada jurado elige a uno
# distinto) el ganador se proclama de manera aleatoria.

def determinar_ganador(matriz_votos: list) -> list:

    ordenar_matriz_por_promedio(matriz_votos, "DESC")
    
    #CASO UNCIO GANADOR
    mejor_promedio = calcular_promedio(matriz_votos, 0)  
    ganadores = []  
    
    for i in range(len(matriz_votos)):
        if calcular_promedio(matriz_votos, i) == mejor_promedio:
            ganadores = ganadores + [matriz_votos[i]]
        else:
            break  

    if len(ganadores) == 1:
        print(f"El ganador es el participante NRO {ganadores[0][I_NUMERO]} ")
        return ganadores[0]

    #CASO DESEMPATE
    print("\n HAY DESEMPATE: ELIJA UN GANADOR (1 O 2), SI ESTA INDECISO SELECCIONE 0 Y SE DECIDIRA AUTOMATICAMENTE")
    indice = 0  
    for participante in ganadores:  
        promedio = calcular_promedio(matriz_votos, indice)  
        print(f"Participante NRO {participante[I_NUMERO]}, Promedio: {promedio}")
        indice += 1 

    votos_jurados = [0] * len(ganadores)  

    for jurado in range(1, 4): 
        voto = pedir_numero_rango(
            f"Ingrese el número del participante (0-{len(ganadores)}): ",
            f"ERROR. Elija un número entre 0 (indeciso) 1 o {len(ganadores)}.",
            0,
            len(ganadores),
        )
        votos_jurados[voto - 1] += 1  

    max_votos = votos_jurados[0]
    ganador_i = 0

    for i in range(1, len(ganadores)):
        if votos_jurados[i] > max_votos:
            max_votos = votos_jurados[i]
            ganador_i = i

    empate_votos = 0
    for voto in votos_jurados:
        if voto == max_votos:
            empate_votos += 1
        print(empate_votos) 

    # CASO ALEATORIO
    if empate_votos > 0:
        print("\nLos jurados no lograron decidir, se elegirá aleatoriamente entre los empatados:")
        ganador_i = random.randint(0, len(ganadores) - 1)

    ganador = ganadores[ganador_i]
    print(f"\nEl ganador es: Participante NRO {ganador[I_NUMERO]}")

    return ganador
    




