#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####################################
# Realizado por:                    #
#-----------------------------------#
#                                   #
# Miguel Ruiz                       #
#___________________________________#
#####################################

"""
Práctica 2
    Realizar un programa que permita gestionar listas de correo de interés
"""

import os

# Definición de una funcion para cada menu del programa
def Menu_inicio():

    opcion = 0
    while opcion != "1" and opcion != "2" and opcion != "3":
        opcion = input("Introduce una opcion: "
                           "\n 1. Gestionar una lista de interés."
                           "\n 2. Generar nuevas listas de correo."
                           "\n 3. Salir. \n Opción elegida: ")
    return opcion


def Menu_1():

    opcion = 0
    while opcion != "a" and opcion != "b" and opcion != "c" \
            and opcion != "d" and opcion != "z":
        opcion = input("Introduce una opción: "
                           "\n a. Lista los correos contenidos en un tema."
                           "\n b. Añadir nuevo correo a la lista."
                           "\n c. Eliminar un correo de la lista."
                           "\n d. Modificar un correo existente."
                           "\n z. Salir. \n Opción elegida: ")
    return opcion


def Menu_2():

    opcion = 0
    while opcion != "a" and opcion != "b" and opcion != "c" \
            and opcion != "d" and opcion != "z":
        opcion = input("Introduce una opción: "
                           "\n a. Generar una nueva lista con todos los "
                           "correos de los temas especificados."
                           "\n b. Generar una nueva lista con los correos "
                           "de las personas interesadas en todos los "
                           "temas especificados."
                           "\n c. Comprobar si alguna de las listas "
                           "especificadas coincide con las otras."
                           "\n d. Comprobar si alguna de las listas "
                           "especificadas está contenida en alguna otra."
                           "\n z. Salir. \n Opción elegida: ")
    return opcion


## Definición de una función que crea un conjunto a partir de un fichero y,
## si el fichero no existe, crea un fichero y conjunto vacíos.
def Inicio_conjunto(tema):

    archivo = tema + ".txt"
    try:
        fich = open(archivo, "r+")
    except:
        print ("\tEl tema no existe. Por tanto, se creará uno nuevo.")
        print ("-" * 75)
        open(archivo, "w")
        conj = set()
    else:
        conj = set()
        ## Utilización de la función definida posteriormente para
        ## quitar el retorno de carro y signos de puntuación y convertir
        ## el texto a minúsculas
        for line in fich:
            line = Limpiar_linea(line)
            conj.add(line)
    return conj


## Igual que antes, solo que no creará el tema si este no existe
def Inicio_conjunto2(tema):

    archivo = tema + ".txt"
    try:
        fich = open(archivo, "r+")
    except:
        print ("Error. El tema no existe.")
        tema_n = input("Vuelve a introducir el tema: ")
        conj = Inicio_conjunto2(tema_n)
    else:
        conj = set()
        for line in fich:
            line = Limpiar_linea(line)
            conj.add(line)
    return conj


## Definición de una función que quita el retorno de carro y signos de puntuacion (si se encuentran)
## al final de la línea y convierte el texto a minúsculas.
def Limpiar_linea(line):

    line = line.lower()
    if line.endswith("\n"):
        line = line[:len(line) - 1]
        if line.endswith(",") or line.endswith(".") or line.endswith(";"):
            line = line[:len(line) - 1]
    return line


## Definición de una función que escribe un conjunto en un fichero
def Escribir_conjunto_fich(conjunto, tema):

    fichero = tema + ".txt"
    fich = open(fichero, "w")
    for i in conjunto:
        i += "\n"
        fich.write(i)
    return conjunto


##Definición de una función que devuelve un listado por pantalla
## con los temas que se encuentran en el directorio actual
def Listar_temas_directorio(ruta):

    listaFich = []

    for archivo in os.listdir(ruta):
        nombre = archivo.split(".")
        if nombre[1] == "txt":
            listaFich.append(nombre[0])
    print ("La lista de temas existentes en el directorio actual es: \n")
    for i in listaFich:
        print (i)
    print ("-" * 75)
    return listaFich


## Definición de una función que liste el contenido de un conjunto por pantalla
## Menú 1, opción a.
def Listar_contenido(conjunto):

    for i in conjunto:
        print (i)


## Definición de una función que añade un correo nuevo a un determinado tema
## Menú 1, opción b
def Anyadir_correo(conjunto, tema):

    correo = input("Introduce correo: ")
    conjunto.add(correo)
    correo += "\n"
    Escribir_conjunto_fich(conjunto, tema)
    print ("Se ha añadido el correo ", correo)


## Definición de una función que elimina un correo dado de un tema determinado.
## Menú 1, opción c
def Eliminar_correo(conjunto, tema):

    correo = input("Introduzca el correo elegido: ")
    if correo in conjunto:
        conjunto.remove(correo)
        Escribir_conjunto_fich(conjunto, tema)
        print ("Se ha eliminado el correo", correo)
    else:
        print ("No existe el correo en el tema introducido")


## Definición de una función que modifica un correo existente en un tema dado
## Menú 1, opción d
def Modificar_correo(conjunto, tema):

    correo = input("Introduzca el correo a modificar: ")
    if correo in conjunto:
        correo2 = input("Introduzca el correo nuevo que sustituira al anterior: ")
        conjunto.remove(correo)
        conjunto.add(correo2)
        Escribir_conjunto_fich(conjunto, tema)
        print ("Se ha modificado el correo", correo + " por", correo2)
    else:
        print ("No existe el correo en el tema introducido")


## Definición de una función que crea un listado con todos los correos de los temas introducidos
## Menú 2, opción a
def Union_conj(temas, conjuntos):

    archivo = ""
    conjunto_final = set()
    for i in range(len(conjuntos)):
        conjunto_final = conjuntos[i] | conjunto_final
        if i == 0:
            archivo = temas[i]
        elif i != len(temas):
            archivo = archivo + "_" + temas[i]
        else:
            archivo = temas[i]
    return archivo, conjunto_final


## Definición de una función que crea un listado con los correos en común de varios temas introducidos
## Menú 2, opción b
def Intersect_conj(temas, conjuntos):

    archivo = ""
    conjunto_final = conjuntos[0]
    for i in range(len(conjuntos)):
        conjunto_final = conjuntos[i] & conjunto_final
        if i == 0:
            archivo = temas[i]
        elif i != len(temas):
            archivo = archivo + "_" + temas[i]
        else:
            archivo = temas[i]
    return archivo, conjunto_final


## Definición de una función que comprueba si las lista de correos de varios temas coinciden
## Menú 2, opción c
def Dif_sim(temas, conjuntos):

    for i in range(len(conjuntos)-1):
        for j in range(i + 1, len(conjuntos)):
            conj = conjuntos[i] ^ conjuntos[j]
            if conj:
                print ("La lista " + temas[i] + " y la lista " +\
                      temas[j] + " son diferentes.")
            else:
                print ("La lista " + temas[i] + " y la lista " +\
                      temas[j] + " son iguales.")


## Definición de una función que comprueba si hay listas que están contenidas en otras
## Menú 3, opción d
def Subset_conj(temas, conjuntos):

    for i in range(len(conjuntos)):
        for j in range(len(conjuntos)):
            if i != j:
                if conjuntos[i].issubset(conjuntos[j]):
                    print ("La lista " + temas[i] + \
                          " está contenida en la lista " + temas[j])
                else:
                    print ("La lista " + temas[i] + \
                          " no está contenida en la lista " + temas[j])


## Programa principal
def main():

    print ("-" * 75)
    print ("El presente programa permite gestionar listas de correo de" \
          " temas de interés.")
    print ("-" * 75)

    wkdir = input ("Para empezar, introduce la ruta del directorio donde se encuentran"\
                    " los archivos con los que quieres trabajar: ")
    os.chdir(wkdir)

    ## Menú principal (inicio)
    opcion = Menu_inicio()

    ## Si la opción es 1, se accede al menú 1
    if opcion == "1":
        print ("\n"+("-" * 75))
        print ("Gestionar una lista de interés.")
        print ("-" * 75)

        print ("\tLos temas a elegir son:\n")
        with os.scandir(wkdir) as ficheros:
            for fichero in ficheros:
                print(fichero.name)
        tema = input ("\nIntroduzca un tema a gestionar sin incluir la extensión del archivo: ")
                     
        print ("-" * 75)

        ## Se crea un conjunto con los emails del tema seleccionado
        conj = Inicio_conjunto(tema)
        opc_1 = Menu_1()
        if opc_1 == "a":
            print ("-" * 75)
            print ("Lista de correos interesados en", tema)
            Listar_contenido(conj)
        elif opc_1 == "b":
            print ("-" * 75)
            print ("Añadir un correo a una lista de interés")
            Anyadir_correo(conj, tema)
        elif opc_1 == "c":
            print ("-" * 75)
            print ("Eliminar un correo de una lista de interés")
            Eliminar_correo(conj, tema)
        elif opc_1 == "d":
            print ("-" * 75)
            print ("Modificar un correo de una lista de interés")
            Modificar_correo(conj, tema)

    ## Si la opción es 2, se accede al menú 2
    elif opcion == "2":
        print ("-" * 75)
        print ("\t Generar nuevas listas de correo.")
        print ("-" * 75)

        Listar_temas_directorio(wkdir)
        temas = int(input("Introduce el número de temas: "))
        lista_temas = []
        lista_conj = []
        for i in range(temas):
            tema = input('Selecciona un tema ' + str(i + 1) + ": ")
            lista_temas.append(tema)
            conj = Inicio_conjunto2(tema)
            lista_conj.append(conj)
        print ("-" * 75)

        opc_2= Menu_2()
        if opc_2 == "a":
            print ("-" * 75)
            print ("Generar una nueva lista con todos los correos de los " \
                  "temas especificados.")
            tema, conj = Union_conj(lista_temas, lista_conj)
            Escribir_conjunto_fich(conj, tema)

        elif opc_2 == "b":
            print ("-" * 75)
            print ("Generar una nueva lista con los correos de las " \
                  "personas interesadas en todos los temas especificados.")
            tema, conj = Intersect_conj(lista_temas, lista_conj)
            Escribir_conjunto_fich(conj, tema)

        elif opc_2 == "c":
            print ("-" * 75)
            print ("Comprobar si alguna de las listas especificadas" \
                  " coincide con las otras.")
            Dif_sim(lista_temas, lista_conj)

        elif opc_2 == "d":
            print ("-" * 75)
            print ("Comprobar si alguna de las listas especificadas " \
                  "esta contenida en alguna de las otras.")
            Subset_conj(lista_temas, lista_conj)
    input("\nPulse <intro> para finalizar")

if __name__ == '__main__':
    main()
