#!/usr/bin/python
# -*- coding: utf-8 -*-

############################################
# -----------------                        #
# Grupo Eds_Gr04:  |                       #
# -----------------------------------------#
# -Miguel Ruiz                             #
#                                          #
############################################

def Glosa(fichero):
    """
    Abre un fichero, lo lee y crea un diccionario con aquellas
    palabras que tienen 4 o más letras indicando la línea en la que se encuentran.
        
    Returns:
        glosario (dict): Diccionario con las palabras de 4 o más letras 
        cuya clave es la palabra y el valor es una lista con las líneas en las que aparece.
    """
    glosario = {}
     
    f = open(fichero, "r")
    nlinea = 0

    finLeer = False
    while not finLeer:
        nlinea += 1
        linea = f.readline()
        if linea == "":
            f.close()
            finLeer = True
        else:
            palabras_signos = linea.split()
            palabras = eliminaSig(palabras_signos)
            for palabra in palabras:
                if len(palabra) >= 4:
                    if palabra not in glosario:
                        glosario[palabra] = [nlinea]
                    elif nlinea not in glosario[palabra]:
                        glosario[palabra].append(nlinea)
    
    return glosario

def eliminaSig(lpalabras):   
    """
    Elimina los signos de puntuación de la lista con las palabras leídas.

    Returns:
        lpalabras: lista con las palabras de la lista sin los signos de 
        puntuación.
    """
    
    for i in range(len(lpalabras)):
        while lpalabras[i].endswith((".",",",";",":","'","\"",")","]","?","!",
                                     "—","…")):
            lpalabras[i] = lpalabras[i][:-1]
        while lpalabras[i].startswith(("'","\"","[","(","¿","¡","—")):
            lpalabras[i] = lpalabras[i][1:]
            
    return lpalabras
            
def main():
    print()
    print("Este fichero crea un fichero de texto con un glosario con las palabras que contienen \
4 o más letras y las líneas en las que se encuentran")
    print ()
    fichero = input("Introduzca el nombre del archivo (incluyendo la ruta): ")

    # Creamos el glosario
    glosario = Glosa(fichero)    
    
    # Abrimos el fichero de salida y volcamos el contenido del diccionario
    f_out = fichero[:-3] + "glo.txt"    
    f2 = open(f_out, "w")
    
    for clave, valor in glosario.items():
        f2.write("%s: %s\n" %(clave,valor))
    
    f2.close()
    
    print ("\n\tSe ha creado el fichero %s exitosamente." % (f_out))
    print ()
    input ("Pulse <INTRO> para finalizar.")
    
if __name__ == "__main__":
    main()
