# Principio de inteligencia artificial trabajando con algoritmos geneticos
# Algoritmo genetico que trata sobre busqueda de un arreglo definido como cromosoma para seleccionar al mejor individuo con mejores
# aptitudes para la musica


# Comienza el codigo

import random
import tkinter as tk
import time

start=time.time()

individuos = int(input("DIGITE EL NUMERO DE INDIVIDUOS: "))
cromosomas = 6
generaciones = int(input("DIGITE EL NUMERO DE GENERACIONES: "))

#Creando un arreglo tamaño de individuos por numero de cromosomas
poblacion = [[0 for x in range(cromosomas)] for x in range(individuos)]

print("POBLACION INICIAL")

#Llenando la población aleatoriamente
for individuo in range(individuos):
    for cromosoma in range(cromosomas):
        poblacion[individuo][cromosoma] = random.randint(0, 1)


#Función para medir aptitud
def medir_aptitud(poblacion):
    aptitud = [0 for i in range(individuos)]
    valores = ["Signo", 2 ** 3, 2 ** 2, 2 ** 1, 2 ** 0, 2 ** -1, 2 ** -2]
    print("")
    print("VALORES PARA DETERMIANR APTITUD MUSICAL")
    print(valores)

# Multiplicndo el Vector de Aptitud por el cromosoma ( fila) de cada individuo de la Poblacion.
    for individuo in range(individuos):
        for cromosoma in range(1, cromosomas):
            aptitud[individuo] += poblacion[individuo][cromosoma] * valores[cromosoma]
        #Cambiando el signo según valor 
        if poblacion[individuo][0] == 1:
            aptitud[individuo] *= -1

    #Imprimiendo valores de aptitud de cada  fila o cromosoma
    print("")
    print("APTITUD")
    for individuo in range(individuos):
        print(str(individuo) + " - [" + ", ".join(str(f) for f in poblacion[individuo]) + "] = " + "{:.9}".format(aptitud[individuo]))
 
# Imprimiendo la Aptitud Total de la Poblacion ( Sumas de las Aptitudes de sus individuos)
    total_aptitud = 0
    for x in range(individuos):
        total_aptitud += abs(aptitud[x])
    print("TOTAL APTITUD " + str(total_aptitud))
    print("")
    return aptitud


#Función para realizar torneo entre cada par de individuos (elige el individuo con mayor aptitud)
def torneo(indice_individuo1, indice_individuo2):
    print("TORNEO")
    print(str(indice_individuo1) + " - [" + ", ".join(str(f) for f in poblacion[indice_individuo1]) + "] = " + "{:.9}".format(aptitud[indice_individuo1]))
    print(str(indice_individuo2) + " - [" + ", ".join(str(f) for f in poblacion[indice_individuo2]) + "] = " + "{:.9}".format(aptitud[indice_individuo2]))

    if abs(aptitud[indice_individuo1]) > abs(aptitud[indice_individuo2]):
        indice_ganador = indice_individuo1
    else:
        indice_ganador = indice_individuo2

    print("GANADOR")
    print(str(indice_ganador) + " - [" + ", ".join(str(f) for f in poblacion[indice_ganador]) + "] = " + "{:.9}".format(aptitud[indice_ganador]))
    print("")
 
    return indice_ganador


#Función de mutación que cambia de 1 a 0 un bit elegido al azar en un individuo
def mutacion(indice_individuo):
    print("MUTACIÓN")
    print(str(indice_individuo) + " - [" + ", ".join(str(f) for f in poblacion[indice_individuo]) + "]")
    indice_mutado = random.randint(0, cromosomas - 1)
 
    if poblacion[indice_individuo][indice_mutado] == 0:
        poblacion[indice_individuo][indice_mutado] = 1
    else:
        poblacion[indice_individuo][indice_mutado] = 0

    print(str(indice_individuo) + " - [" + ", ".join(str(f) for f in poblacion[indice_individuo]) + "]")
    print("")


#Función de cruce que intercambia un bit de dos individuos,la posicion del bit se elige al azar
def cruce(indice_individuo1, indice_individuo2):
    print("CRUCE")
    print(str(indice_individuo1) + " - [" + ", ".join(str(f) for f in poblacion[indice_individuo1]) + "]")
    print(str(indice_individuo2) + " - [" + ", ".join(str(f) for f in poblacion[indice_individuo2]) + "]")
    indice_cruce = random.randint(1, cromosomas - 1)
    print("Índice de cruce " + str(indice_cruce));
    print("Descendencias")
    descendencia1 = poblacion[indice_individuo1][:indice_cruce] + poblacion[indice_individuo2][indice_cruce:]
    print(descendencia1)
    descendencia2 = poblacion[indice_individuo2][:indice_cruce] + poblacion[indice_individuo1][indice_cruce:]
    print(descendencia2)
    return descendencia1, descendencia2


#Imprime población
def imprime_poblacion():
    for individuo in range(individuos):
        print(str(individuo) + " - [" + ", ".join(str(f) for f in poblacion[individuo]) + "]")


for generacion in range(generaciones):
    print("")
    print("--------- GENERACIÓN " + str(generacion) +" ---------")
    imprime_poblacion()
    nueva_generacion = [0 for x in range(individuos)]
 
    aptitud = medir_aptitud(poblacion)

    for i in range(individuos // 2):
        individuo_ganador = torneo(i, individuos - 1 -i)
        nueva_generacion[i] = poblacion[individuo_ganador]

    mutaciones = random.randint(0, individuos // 2)
    for j in range(mutaciones):
        mutacion(random.randint(0, mutaciones))

    indice_hijos = individuos // 2
    for k in range(0, individuos // 2, 2):
        nueva_generacion[indice_hijos], nueva_generacion[indice_hijos + 1] = cruce(k, k+1)
        indice_hijos += 2
        print("")

    poblacion = nueva_generacion





print("")
print("------- ÚLTIMA GENERACIÓN -------")
imprime_poblacion()
medir_aptitud(poblacion)

end= time.time()
print(end-start)
input()
