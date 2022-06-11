#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################
#                                #
#   Autor : Miguel Ruiz Ibáñez   #
#                                #
##################################

"""
Este programa nos permite jugar a 'Adivina el animal que estoy pensando' 
a partir del fichero 'ANIMALES.ARB' utilizando árboles binarios y recorrido prefijo.
"""

import os 

class Arbol:
    
    def __init__ (self, inf = None, izq = None, der = None):
        if inf == None:
            self.esvacio = True
        else:
            self.esvacio = False
            self.info = inf
            if izq == None:
                self.izdo = Arbol()
            else:
                self.izdo = izq
            if der == None:
                self.dcho = Arbol()
            else:
                self.dcho = der
                
    def Informacion (self):
        return self.info #Devuelve la información contenida en el nodo

    def HijoIzdo (self):
        return self.izdo #Devuelve la info contenida en el hijo izquierdo

    def HijoDcho (self):
        return self.dcho #Devuelve la info contenida en el hijo derecho

    def es_vacio (self):
        return self.esvacio #Devuelve un booleano dependiendo si está vacío (True) o no (False)
        
    
def es_hoja (arbol):
    
    '''
    Esta función nos permite saber si un nodo es hoja o no, y por tanto,
    si tiene hijos. 
    
    Args: 
        Un árbol en el que sus nodos contienen información. 
        
    Returns: 
        hoja (bool) que nos indica si el nodo es hoja o no. 
    '''
    
    hijoderecho = arbol.dcho
    d = hijoderecho.es_vacio()
    hijoizquierdo = arbol.izdo
    i = hijoizquierdo.es_vacio()

    if d == True and i == True:
        hoja = True
        
    else:
        hoja = False
        
    return(hoja)   
    
def abrir_archivo(nombre):
    
    ''' 
    Esta función abre el archivo de nombre indicado y extrae su información, 
    guardándola en una lista, de forma que cada línea del archivo en cuestión 
    es un elemento de la lista. 
    
    Args: 
        Nombre del fichero a partir del cual se va a extrar la información. 
        
    Returns: 
        lista (list) en la que cada elemento es una línea del fichero. 
    '''
    
    try:
        lista = []
        fichero = open(nombre, 'r', encoding = "utf8", errors = 'ignore')
        for line in fichero:
            linea = line.strip()
            #Para eliminar los saltos de línea
            lista.append(linea)
        
        fichero.close()
        return(lista)
        
    except:
        print('No se ha podido abrir el archivo indicado.')
        
def creacion_arbol(lista):
    
    '''
    Función que reconstruye un arbol a partir de una lista.
    
    Precondiciones:
        Dicha lista debe contener el recorrido prefijo del árbol y se ha 
        obtenido ejecutando la función anterior. 
        
    Args:
        Lista con el recorrido prefijo del árbol. 
        
    Returns: 
        Nodo (arbol) reconstruido a partir de su recorrido prefijo. 
    '''
    
    contenido = lista[0]
    del lista[0]
    if contenido == '.':
        nodo = Arbol()
        
        
    else: 
        nodoizq = creacion_arbol(lista)
        nododer = creacion_arbol(lista)
        nodo = Arbol(contenido, nodoizq, nododer)
        
    return(nodo)
    
def guardar_archivo(Arbol, nombre_fich):
    
    """
    Esta función nos premite guardar en un archivo el árbol reconstruido. 
    Este archivo contiene el árbol en recorrido prefijo. 
    """
    archivo = open(nombre_fich, 'a')
    if es_hoja(Arbol) == False:
        
        info = Arbol.Informacion()
        archivo.write(info + '\n')
        archivo.close()
        guardar_archivo(Arbol.HijoIzdo(), nombre_fich)
        guardar_archivo(Arbol.HijoDcho(), nombre_fich)
        
    else:
        info = Arbol.Informacion()
        archivo.write(info + '\n.\n.\n')
        archivo.close()
        
def recorre_arbol(arbol): 
    
    '''
    Función que permite al usuario recorrer el árbol hasta que llega a una
    hoja. En ese caso, la función devuelve la información contenida en la hoja.
    '''

    if es_hoja(arbol) == False:
        info = arbol.Informacion()
        izq = arbol.HijoIzdo()
        der = arbol.HijoDcho()
        respuesta1 = ' '
        while respuesta1 not in ['S','s','N','n']:
            print(info)
            respuesta1 = input('Responde a la pregunta anterior con si (S/s) o no(N/n):\n')
            if respuesta1 == 'S' or respuesta1=='s':
                recorre_arbol(izq)
            elif respuesta1=='N' or respuesta1 == 'n':
                recorre_arbol(der)
    else: 
    
        """
        Cuando es_hoja es True quiere decir que el nodo analizado es el 
        animal que busca el programa. En este punto se mostrará el resultado
        y se preguntará si es correcto.
        """

        info = arbol.Informacion()
        print('\nSE HA ALCANZADO UNA PREDICCIÓN.')
        print('\nSOLUCIÓN: ¿', info, '?', sep='')

        correcto = ' '
        while correcto not in ['S','s','N','n']:    
            correcto = input('¿Se trata del animal que estabas pensando? Responde con si (S/s) o no (N/n): ')

        if correcto == 'S' or correcto == 's':
            print('SE HA ADIVINADO TU ANIMAL.')
        
        elif correcto == "N" or correcto == "n":
        #Si no es correcto, mejoramos el juego. 
            print('NO SE HA ADIVINADO TU ANIMAL.')
            mejorar = ' '
            while mejorar not in ['S','s','N','n']:
                mejorar = input('¿Quieres ayudar al juego a mejorar insertando tu animal en él? Responde con si (S/s) o no (N/n): ')
            
            if mejorar == 'S' or mejorar == 's':
                nueva_respuesta = ' '
                while nueva_respuesta not in ['S','s','n','N']:
                    pregunta = input('¿Que pregunta harias para distinguir tu animal del que ha sugerido el programa? ')
                    nueva_respuesta = input('¿La respuesta a tu nueva pregunta para obtener el animal en el que estabas pensando es si (S/s) o no (N/n)? ')
                    animal = input('¿En que animal estabas pensando? ')
                        
                animal_def = 'es un/a ' + animal
                
                if nueva_respuesta == 'S' or nueva_respuesta == 's':
                    arbol.dcho = Arbol(info)
                    arbol.izdo = Arbol(animal_def)
                    arbol.info = pregunta
                    
                else: 
                    arbol.izdo = Arbol(info)
                    arbol.dcho = Arbol(animal_def)
                    arbol.info = pregunta


def juego (arbol): 
    """
    Esta función muestra la información del juego, lo inicia y, una vez 
    finalizado, pregunta si quiere guardar los cambios.
    """

    print (' -' + '-' * 81)
    print('| BIENVENIDO AL JUEGO "ADIVINA EL ANIMAL EN EL QUE ESTOY PENSANDO":                |')
    print('| El juego consiste en que pienses un animal, y el programa tratará de adivinarlo. |')
    print('| Si consigues ganar al programa, puedes ayudar a mejorarlo.                       |')
    print (' -' + '-' * 81)
    print ('')
    
    recorre_arbol(arbol)
    respuesta = ' '
    while respuesta not in ['S','s','N','n']:
        print('\n')
        respuesta = input('¿Quieres jugar de nuevo? Contesta si (S/s) o no (N/n): ')

        if respuesta not in ['S','s','N','n']:
            print('Respuesta no válida. Por favor, responde correctamente.')
        
    if respuesta == 's' or respuesta=='S':
        juego(arbol)


def main(): 

    os.chdir ("/Users/miguelruizibanez/Documents/Trabajos_Bioinf/EBD/ED")

    lista_prefijo = abrir_archivo('ANIMALES.ARB') 
   
    arbol = creacion_arbol(lista_prefijo)
    
    juego(arbol)
    
    guardar = ' '
    while guardar not in ['S','s','N','n']:
        guardar = input('¿DESEAS GUARDAR LOS CAMBIOS INTRODUCIDOS? Responde sí (S/s) o no (N/n)')
        
    if guardar == 's' or guardar == 'S':
        nombre_archivo = 'ANIMALES.ARB'
        try:
            os.remove (nombre_archivo)
        except:
            print('ERROR: No existe el fichero.')
        
        guardar_archivo(arbol, nombre_archivo)
        print('LOS CAMBIOS HAN SIDO GUARDADOS.')
    
    print ('')
    print('GRACIAS POR JUGAR, ¡VUELVE PRONTO!')
    
if __name__ == '__main__': 
    main()