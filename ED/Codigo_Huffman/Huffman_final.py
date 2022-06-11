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
PRÁCTICA 3: CÓDIGOS DE HUFFMAN. Este programa codifica y decodifica un texto con códigos de Huffman.
"""

import sys
from typing import TextIO 

class Arbol:
 
    def __init__(self, raiz=None, izdo = None, dcho = None):
        if raiz is None:
            self.esvacio = True
        else:
            self.esvacio = False
            self.info = raiz
            if izdo is None:
                self.izdo = Arbol()
            else:
                self.izdo = izdo
            if dcho is None:
                self.dcho = Arbol()
            else:
                self.dcho = dcho

    def Informacion (self): 
        """
        Nos proporciona información del contenido del árbol.
        """
        return self.info

    def HijoIzdo (self):
        """
        Nos proporciona la información del contenido del subárbol izquierdo.
        """
        return self.izdo
    
    def HijoDcho (self):
        """
        Nos proporciona la información del contenido del subárbol derecho.
        """
        return self.dcho

    def ArbolVacio (self):
        """
        Nos proporciona información sobre si el árbol está vacío o no.
        """
        return self.esvacio

    def __lt__(self, arbol_2):
        """
        Compara la información de dos árboles y devuelve True si 
        el el árbol self es menor que el arbol_2

        Returns:
            bool: True Si self es menor a arbol_2
                  False Si self no es menor a arbol_2
        """
        if self.Informacion() < arbol_2.Informacion():
            menor = True
        else:
            menor = False
            
        return menor
    
    def __eq__(self, arbol_2): 
        """
        Compara la información del árbol self con la del arbol_2 y 
        devuelve True si son iguales.

        Returns:
            bool: True Si self es igual a arbol_2
                  False Si self no es menor a arbol_2
        """
        if self.Informacion() == arbol_2.Informacion():
            igual = True
        else:
            igual = False
            
        return igual


class Informacion:
    """
    Clase contenida en la Información del árbol de Huffman
    """
    def __init__(self, caracter, frec): 
        self.caracter = caracter   
        self.frec = frec   
    
    def __lt__(self, informacion_2): 
        """
        Compara el objeto Informacion self con informacion_2 y devuelve
        True si la frecuencia de self es menor que la de informacion_2.

        Returns:
            bool: True Si self es menor a informacion_2
                  False Si self no es menor a arbol_2
        """
        if self.frec < informacion_2.frec: 
            menor = True
        else:
            menor = False
        return menor
    
    def __eq__(self, informacion_2): 
        """
        Compara el objeto Informacion self con informacion_2 y devuelve
        True si sus frecuencias son iguales.

        Returns:
            bool: True Si self es igual a informacion_2
                  False Si self no es igual a arbol_2
        """
        if self.frec == informacion_2.frec:
            igual = True
        else:
            igual = False
        
        return igual


def AbrirFichero(nom_fich_entrada):
    """
    Función para abrir ficheros.
    """
    try:
        fichero = open(nom_fich_entrada + ".txt", "r")
    except:
        print("Se ha producido un error intentando abrir el fichero.")
        sys.exit()     
    return fichero

def ContarCaracteres(fichero):
    """
    Cuenta los caracteres contenidos en un fichero.
    Recoge la información en un diccionario.

    Return:
       Diccionario con los caracteres como claves y sus respectivas
       frecuencias absolutas como valor.
    """
    dicc_caracteres = {}
    for linea in fichero:
        for caracter in linea:
            if caracter in dicc_caracteres:
                dicc_caracteres[caracter] += 1
            else:
                dicc_caracteres[caracter] = 1
    
    return dicc_caracteres

def CrearBosque(dicc_caracteres):
    """
    Crea un lista de árboles a partir de un dicciorio.
    Los nodos de los árboles son objetos de la clase Información 
    que tienen como atributos el caracter y la frecuencia de cada
    uno de los elementos del diccionario. Sus hijos izquierdos y derechos
    son árboles vacíos.

    Return:
        lista de árboles
    """
    bosque = []
    for caracter in dicc_caracteres:
        info = Informacion(caracter, dicc_caracteres[caracter])
        arbol = Arbol(info)
        bosque.append(arbol)

    return bosque

def ConstruirArbolHuffman(bosque):
    """
    Genera el árbol de Huffman a partir del bosque de árboles
    que contienen los caracteres y sus frecuencias en sus nodos.

    Returns:
        árbol de Huffman
    """
    while len(bosque) != 1:
        bosque.sort()
        primer_menor = bosque.pop(0)
        segundo_menor = bosque.pop(0)
        frec = (primer_menor.Informacion().frec 
                + segundo_menor.Informacion().frec)  
        info = Informacion("\7", frec)
        arbol = Arbol(info, primer_menor, segundo_menor)
        bosque.append(arbol)             

    return bosque[0]
 
def CrearDiccCodigos(arbol, codigo, dicc):
    """
    Crea un diccionario que contiene como claves caracteres y como 
    valores su codificación. Se construye a partir del recorrido del
    árbol de Huffman.

    Return:
        dicc: diccionario de caracteres y códigos 
    """
    if arbol.Informacion().caracter == "\7":
        CrearDiccCodigos(arbol.HijoIzdo(), codigo + "0", dicc)
        CrearDiccCodigos(arbol.HijoDcho(), codigo + "1", dicc)                      
    else:
        dicc[arbol.Informacion().caracter] = codigo
   
    return dicc 

def IniciarDiccCodigos(arbol):
    """
    Inicia el diccionario y la subcadena de código.

    Return:
        diccionario de caracteres y códigos
    """
    codigo = ""
    dicc_codigos = {}
    dicc_codigos = CrearDiccCodigos(arbol, codigo, dicc_codigos)

    return dicc_codigos
    
def CodificarFichero(arb, nom_fich_in, nom_fich_out, dicc_cod):
    """
    Codifica un fichero.
    """
    archivo_codificado = open(nom_fich_out + ".txt", "w")
    GuardarCabecera(arb, archivo_codificado)
    CodificarTexto(nom_fich_in, archivo_codificado, dicc_cod)
    archivo_codificado.close()
    
    return

def GuardarCabecera(arb, archivo_codificado):
    """
    Almacena el árbol de códigos de Huffman como cabecera del 
    fichero de salida.
    """
    if not arb.ArbolVacio():
        info = arb.Informacion().caracter
        archivo_codificado.write(info)
        GuardarCabecera(arb.HijoIzdo(), archivo_codificado)
        GuardarCabecera(arb.HijoDcho(), archivo_codificado)
    
    return

def CodificarTexto(nom_fich_in, archivo_codificado, dicc_cod):
    """
    Codifica un fichero a partir de los códigos de Huffman.
    """
    fich = open(nom_fich_in + ".txt", "r")
    fin_fich = False
    while not fin_fich:
        char = fich.read(1)
        if char == "":
            fin_fich = True
        else:
            archivo_codificado.write(dicc_cod[char])
    
    return

def DecodificarFichero(fich_in, nom_fich_out):
    """
    Decodifica un fichero.
    """
    arbol_huffman = ReconstruirArbol(fich_in)
    DecodificarTexto(fich_in, arbol_huffman, nom_fich_out)
    fich_in.close()
    
    return
    
def ReconstruirArbol(fich_in):
    """
    Reconstruye el árbol de códigos de Huffman a partir de la 
    cabecera del archivo codificado.

    Returns:
        arbol (Arbol): Árbol con los códigos de Huffman
    """
    char = fich_in.read(1)
    if char == "\7":
        arb_izdo = ReconstruirArbol (fich_in)
        arb_dcho = ReconstruirArbol (fich_in)
        arbol = Arbol(char, arb_izdo, arb_dcho)
    else:
        arbol = Arbol(char)
    
    return arbol

def DecodificarTexto(fich_in, arbol, nom_fich_out):
    """
    Decodifica el texto a partir de los códigos de Huffman
    y guarda la información en un fichero.
    """
    archivo_decodificado = open(nom_fich_out + ".txt", "a")
    arbol_original = arbol
    fin_fich = False
    while not fin_fich:
        char = fich_in.read(1)
        if char == "":
            fin_fich = True
            archivo_decodificado.write(arbol.Informacion())
        else:
            if arbol.Informacion() != "\7": 
                archivo_decodificado.write(arbol.Informacion())
                arbol = arbol_original
            if char == "0":
                arbol = arbol.HijoIzdo()
            elif char == "1":
                arbol = arbol.HijoDcho()        
    
    return

def main():
    
    print("Este programa codifica y descodifica un fichero mediante códigos de Huffman.") 
    opcion=""
    opciones = ("1", "2")
    repetir= True
    while repetir:
        while opcion not in opciones:
            print("Introduzca la opción que desea realizar: ")
            opcion=input("¿Desea codificar (1) o descodificar (2)?: ")

        if opcion == "1":
            nom_fich_in = input("Introduzca el nombre del fichero a codificar sin extensión: ")
            nom_fich_out = input("Introduzca un nombre para el fichero de salida: ")
            fich = AbrirFichero(nom_fich_in)
            dicc_char = ContarCaracteres(fich)
            bosque = CrearBosque(dicc_char)
            arbol = ConstruirArbolHuffman(bosque)
            dicc_codigos = IniciarDiccCodigos(arbol)
            CodificarFichero(arbol, nom_fich_in, nom_fich_out, dicc_codigos)

        if opcion == "2":
            nom_fich_in = input("Introduzca el nombre del fichero a descodificar sin extensión: ")
            nom_fich_out = input("Introduzca un nombre para el fichero de salida: ")
            fich_in = AbrirFichero(nom_fich_in)
            DecodificarFichero(fich_in, nom_fich_out)

        opcion2=""
        opciones2 = ("Si", "No")
        while opcion2 not in opciones2:
            opcion2=input("¿Quieres realizar otra operación? (Si/No): ")

        if opcion2 == "Si":
            repetir = True
            opcion = ""
        else:
            repetir = False

    input("Pulse <Intro> para finalizar.")

if __name__=="__main__":
    main()
